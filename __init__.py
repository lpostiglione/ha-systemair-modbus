from __future__ import annotations
from datetime import timedelta
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.const import Platform

from .const import (
    DOMAIN, DEFAULT_NAME,
    CONF_HOST, CONF_PORT, CONF_UNIT_ID, CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
    REG_FAN_SPEED_LEVEL, REG_FAN_SF_RPM, REG_FAN_EF_RPM,
    REG_HC_TEMP_LVL, REG_HC_TEMP_SP,
    REG_HC_TEMP_IN1, REG_HC_TEMP_IN2, REG_HC_TEMP_IN4, REG_HC_TEMP_IN5,
    REG_ROTOR_STATE, REG_FILTER_PER, REG_FILTER_DAYS,
)

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[Platform] = [Platform.FAN, Platform.SENSOR, Platform.SELECT]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Systemair from a config entry."""
    host = entry.data[CONF_HOST]
    port = entry.data[CONF_PORT]
    unit = entry.data[CONF_UNIT_ID]
    scan_interval = entry.options.get(CONF_SCAN_INTERVAL, entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL))

    coordinator = SystemairCoordinator(hass, host, port, unit, scan_interval)
    await coordinator.async_setup()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = {
        "name": entry.title or DEFAULT_NAME,
        "coordinator": coordinator,
        "unit": unit,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id, None)
    return unload_ok


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

    async def async_setup(self):
        from pymodbus.client import AsyncModbusTcpClient
        self.client = AsyncModbusTcpClient(self._host, port=self._port)
        await self.client.connect()

    async def _async_update_data(self):
        if not self.client or not self.client.connected:
            await self.client.connect()
        try:
            # Blocked reads to minimize roundtrips
            rr1 = await self.client.read_holding_registers(address=100, count=12, slave=self.unit)  # 101,111,112
            rr2 = await self.client.read_holding_registers(address=206, count=12, slave=self.unit)  # 207,208,214..218
            rr3 = await self.client.read_holding_registers(address=350, slave=self.unit)  # 351
            rr4 = await self.client.read_holding_registers(address=600, count=2, slave=self.unit)  # 601,602

            if any(r.isError() for r in (rr1, rr2, rr3, rr4)):
                raise UpdateFailed("Modbus read error")

            data: dict[int, int] = {}

            def get(rr, base, reg):
                return rr.registers[reg - base]

            data[REG_FAN_SPEED_LEVEL] = get(rr1, 101, REG_FAN_SPEED_LEVEL)
            data[REG_FAN_SF_RPM] = get(rr1, 101, REG_FAN_SF_RPM)
            data[REG_FAN_EF_RPM] = get(rr1, 101, REG_FAN_EF_RPM)

            data[REG_HC_TEMP_LVL] = get(rr2, 207, REG_HC_TEMP_LVL)
            data[REG_HC_TEMP_SP] = get(rr2, 207, REG_HC_TEMP_SP)
            data[REG_HC_TEMP_IN1] = get(rr2, 207, REG_HC_TEMP_IN1)
            data[REG_HC_TEMP_IN2] = get(rr2, 207, REG_HC_TEMP_IN2)
            data[REG_HC_TEMP_IN4] = get(rr2, 207, REG_HC_TEMP_IN4)
            data[REG_HC_TEMP_IN5] = get(rr2, 207, REG_HC_TEMP_IN5)

            data[REG_ROTOR_STATE] = rr3.registers[0]

            data[REG_FILTER_PER] = get(rr4, 601, REG_FILTER_PER)
            data[REG_FILTER_DAYS] = get(rr4, 601, REG_FILTER_DAYS)

            return data
        except Exception as err:
            raise UpdateFailed(err) from err

    async def async_write_register(self, address: int, value: int):
        if not self.client or not self.client.connected:
            await self.client.connect()
        # Adjust 1-based register address from docs to 0-based for pymodbus
        await self.client.write_register(address=(address - 1), value=value, slave=self.unit)
