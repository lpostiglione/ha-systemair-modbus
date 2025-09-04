from __future__ import annotations
from datetime import timedelta
import logging
import asyncio

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import (
    REG_FAN_SPEED_LEVEL, REG_FAN_SF_PWM, REG_FAN_EF_PWM, REG_FAN_SF_RPM, REG_FAN_EF_RPM,
    REG_HC_HEATER_TYPE, REG_HC_COOLER_TYPE, REG_HC_WC_SIGNAL, REG_HC_WH_SIGNAL,
    REG_HC_TEMP_LVL, REG_HC_TEMP_SP,
    REG_HC_TEMP_IN1, REG_HC_TEMP_IN2, REG_HC_TEMP_IN3, REG_HC_TEMP_IN4, REG_HC_TEMP_IN5, REG_HC_PREHEATER_TYPE,
    REG_ROTOR_STATE, REG_DAMPER_PWM, REG_FILTER_PER, REG_FILTER_DAYS,
    REG_RH_SENSOR_VALUE, REG_RH_SENSOR_DATA_VALID, REG_RH_SENSOR_PRESENT,
    REG_SYSTEM_TYPE, REG_SYSTEM_PROG_V_HIGH, REG_SYSTEM_PROG_V_MID, REG_SYSTEM_PROG_V_LOW,
    REG_SYSTEM_BOOT_PROG_V_HIGH, REG_SYSTEM_BOOT_PROG_V_MID, REG_SYSTEM_BOOT_PROG_V_LOW,
    REG_SYSTEM_PROG_STATE,
)

_LOGGER = logging.getLogger(__name__)


class SystemairCoordinator(DataUpdateCoordinator[dict[int, int]]):
    """Coordinator that polls required registers in block reads."""

    def __init__(self, hass: HomeAssistant, host: str, port: int, unit: int, scan_interval: int):
        super().__init__(
            hass,
            _LOGGER,
            name="systemair coordinator",
            update_interval=timedelta(seconds=scan_interval),
        )
        self._host = host
        self._port = port
        self.unit = unit
        self.client = None
        # Serialize all Modbus operations to avoid overlapping I/O and reconnect storms
        self._io_lock = asyncio.Lock()
        self._connect_lock = asyncio.Lock()

    async def async_setup(self):
        # Create client here; connection will be established on first use
        from pymodbus.client import AsyncModbusTcpClient
        self.client = AsyncModbusTcpClient(self._host, port=self._port)
        # Don't call connect twice; _ensure_connected handles it
        await self._ensure_connected()

    async def _ensure_connected(self):
        # Ensure a single connect attempt at a time
        async with self._connect_lock:
            if self.client is None:
                from pymodbus.client import AsyncModbusTcpClient
                self.client = AsyncModbusTcpClient(self._host, port=self._port)
            if not getattr(self.client, "connected", False):
                try:
                    ok = await self.client.connect()
                    if not ok and not getattr(self.client, "connected", False):
                        raise ConnectionError("Modbus client failed to connect")
                except Exception as err:
                    # Surface as UpdateFailed in callers
                    raise UpdateFailed(f"Modbus connect error: {err}") from err

    async def async_close(self):
        # Close the client gracefully on unload
        client = self.client
        self.client = None
        if client is not None:
            close = getattr(client, "close", None)
            try:
                if close is not None:
                    res = close()
                    if hasattr(res, "__await__"):
                        await res
            except Exception:
                pass

    async def _async_update_data(self):
        # Never allow concurrent I/O; keep the connection and all reads within the lock
        async with self._io_lock:
            await self._ensure_connected()
            try:
                # Blocked reads to minimize roundtrips
                # 101..112 (includes fan speed level, SF/EF PWM, SF/EF RPM)
                rr1 = await self.client.read_holding_registers(address=100, count=12, unit=self.unit)
                # 201..220 (heater/cooler types, signals, temp level/sp, temps in1..in5, preheater type)
                rr2 = await self.client.read_holding_registers(address=200, count=20, unit=self.unit)
                # 351 (rotor state)
                rr3 = await self.client.read_holding_registers(address=350, count=1, unit=self.unit)
                # 301 (damper pwm)
                rr_damper = await self.client.read_holding_registers(address=300, count=2, unit=self.unit)
                # 381..383 (RH value + data valid)
                rr_rh = await self.client.read_holding_registers(address=380, count=4, unit=self.unit)
                # 651..655 (defrosting/RH presence)
                rr_defr = await self.client.read_holding_registers(address=650, count=6, unit=self.unit)
                # 601..602 (filter info)
                rr4 = await self.client.read_holding_registers(address=600, count=2, unit=self.unit)
                # 501..508 (system parameters)
                rr_sys = await self.client.read_holding_registers(address=500, count=8, unit=self.unit)

                if any(r.isError() for r in (rr1, rr2, rr3, rr_damper, rr_rh, rr_defr, rr4, rr_sys)):
                    raise UpdateFailed("Modbus read error")

                data: dict[int, int] = {}

                def get(rr, base, reg):
                    return rr.registers[reg - base - 1]

                # Fan
                data[REG_FAN_SPEED_LEVEL] = get(rr1, 100, REG_FAN_SPEED_LEVEL)
                data[REG_FAN_SF_PWM] = get(rr1, 100, REG_FAN_SF_PWM)
                data[REG_FAN_EF_PWM] = get(rr1, 100, REG_FAN_EF_PWM)
                data[REG_FAN_SF_RPM] = get(rr1, 100, REG_FAN_SF_RPM)
                data[REG_FAN_EF_RPM] = get(rr1, 100, REG_FAN_EF_RPM)

                # Heating/Cooling types and signals, temps
                data[REG_HC_HEATER_TYPE] = get(rr2, 200, REG_HC_HEATER_TYPE)
                data[REG_HC_COOLER_TYPE] = get(rr2, 200, REG_HC_COOLER_TYPE)
                data[REG_HC_WC_SIGNAL] = get(rr2, 200, REG_HC_WC_SIGNAL)
                data[REG_HC_WH_SIGNAL] = get(rr2, 200, REG_HC_WH_SIGNAL)
                data[REG_HC_TEMP_LVL] = get(rr2, 200, REG_HC_TEMP_LVL)
                data[REG_HC_TEMP_SP] = get(rr2, 200, REG_HC_TEMP_SP)
                data[REG_HC_TEMP_IN1] = get(rr2, 200, REG_HC_TEMP_IN1)
                data[REG_HC_TEMP_IN2] = get(rr2, 200, REG_HC_TEMP_IN2)
                data[REG_HC_TEMP_IN3] = get(rr2, 200, REG_HC_TEMP_IN3)
                data[REG_HC_TEMP_IN4] = get(rr2, 200, REG_HC_TEMP_IN4)
                data[REG_HC_TEMP_IN5] = get(rr2, 200, REG_HC_TEMP_IN5)
                data[REG_HC_PREHEATER_TYPE] = get(rr2, 200, REG_HC_PREHEATER_TYPE)

                # Rotor
                data[REG_ROTOR_STATE] = get(rr3, 350, REG_ROTOR_STATE)

                # Damper
                data[REG_DAMPER_PWM] = get(rr_damper, 300, REG_DAMPER_PWM)

                # RH
                data[REG_RH_SENSOR_VALUE] = get(rr_rh, 380, REG_RH_SENSOR_VALUE)
                data[REG_RH_SENSOR_DATA_VALID] = get(rr_rh, 380, REG_RH_SENSOR_DATA_VALID)
                data[REG_RH_SENSOR_PRESENT] = get(rr_defr, 650, REG_RH_SENSOR_PRESENT)

                # Filter
                data[REG_FILTER_PER] = get(rr4, 600, REG_FILTER_PER)
                data[REG_FILTER_DAYS] = get(rr4, 600, REG_FILTER_DAYS)

                # System parameters
                data[REG_SYSTEM_TYPE] = get(rr_sys, 500, REG_SYSTEM_TYPE)
                data[REG_SYSTEM_PROG_V_HIGH] = get(rr_sys, 500, REG_SYSTEM_PROG_V_HIGH)
                data[REG_SYSTEM_PROG_V_MID] = get(rr_sys, 500, REG_SYSTEM_PROG_V_MID)
                data[REG_SYSTEM_PROG_V_LOW] = get(rr_sys, 500, REG_SYSTEM_PROG_V_LOW)
                data[REG_SYSTEM_BOOT_PROG_V_HIGH] = get(rr_sys, 500, REG_SYSTEM_BOOT_PROG_V_HIGH)
                data[REG_SYSTEM_BOOT_PROG_V_MID] = get(rr_sys, 500, REG_SYSTEM_BOOT_PROG_V_MID)
                data[REG_SYSTEM_BOOT_PROG_V_LOW] = get(rr_sys, 500, REG_SYSTEM_PROG_V_LOW)
                data[REG_SYSTEM_PROG_STATE] = get(rr_sys, 500, REG_SYSTEM_PROG_STATE)

                return data
            except Exception as err:
                raise UpdateFailed(err) from err

    async def async_write_register(self, address: int, value: int):
        # Serialize write with other IO and ensure connection
        async with self._io_lock:
            await self._ensure_connected()
            # Adjust 1-based register address from docs to 0-based for pymodbus
            await self.client.write_register(address=(address - 1), value=value, slave=self.unit)
