from __future__ import annotations
from dataclasses import dataclass
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from homeassistant.helpers.entity import EntityCategory
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .entity import SystemairEntity

from .const import (
    DOMAIN, SCALE_TENTH,
    REG_FAN_SF_RPM, REG_FAN_EF_RPM,
    REG_HC_TEMP_SP, REG_HC_TEMP_IN1, REG_HC_TEMP_IN2, REG_HC_TEMP_IN4, REG_HC_TEMP_IN5,
    REG_ROTOR_STATE, REG_FILTER_PER, REG_FILTER_DAYS,
    ROTOR_STATE_MAP,
    REG_SYSTEM_TYPE, REG_SYSTEM_PROG_V_HIGH, REG_SYSTEM_PROG_V_MID, REG_SYSTEM_PROG_V_LOW,
    REG_SYSTEM_BOOT_PROG_V_HIGH, REG_SYSTEM_BOOT_PROG_V_MID, REG_SYSTEM_BOOT_PROG_V_LOW,
    REG_SYSTEM_PROG_STATE, SYSTEM_TYPE_MAP,
)

@dataclass
class SensorDesc:
    name: str
    reg: int
    unit: str | None = None
    device_class: str | None = None
    scale: float | None = None


SENSORS: list[SensorDesc] = [
    SensorDesc("Systemair Heating Target", REG_HC_TEMP_SP, "°C", SensorDeviceClass.TEMPERATURE, None),
    SensorDesc("Systemair Supply Air Temp", REG_HC_TEMP_IN1, "°C", SensorDeviceClass.TEMPERATURE, SCALE_TENTH),
    SensorDesc("Systemair Extract Air Temp", REG_HC_TEMP_IN2, "°C", SensorDeviceClass.TEMPERATURE, SCALE_TENTH),
    SensorDesc("Systemair Overheat/Frost Temp", REG_HC_TEMP_IN4, "°C", SensorDeviceClass.TEMPERATURE, SCALE_TENTH),
    SensorDesc("Systemair Outdoor Air Temp", REG_HC_TEMP_IN5, "°C", SensorDeviceClass.TEMPERATURE, SCALE_TENTH),
    SensorDesc("Systemair Supply Fan RPM", REG_FAN_SF_RPM, "rpm", None, None),
    SensorDesc("Systemair Extract Fan RPM", REG_FAN_EF_RPM, "rpm", None, None),
    SensorDesc("Systemair Rotor State (raw)", REG_ROTOR_STATE, None, None, None),
    SensorDesc("Systemair Filter Period", REG_FILTER_PER, "months", None, None),
    SensorDesc("Systemair Filter Days Since Change", REG_FILTER_DAYS, "days", None, None),
]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coord = data["coordinator"]
    name = data["name"]
    entities = [SystemairRegisterSensor(coord, name, d) for d in SENSORS]
    entities.append(SystemairRotorStateText(coord, name))  # friendly rotor text

    # Diagnostic sensors (disabled by default)
    entities.extend([
        SystemairDiagnosticText(coord, name, "Systemair Model", lambda d: SYSTEM_TYPE_MAP.get(int(d.get(REG_SYSTEM_TYPE))) if d.get(REG_SYSTEM_TYPE) is not None else None),
        SystemairDiagnosticNumber(coord, name, "Systemair System Type", REG_SYSTEM_TYPE),
        SystemairDiagnosticText(coord, name, "Systemair Firmware Version", lambda d: _fmt_ver(d.get(REG_SYSTEM_PROG_V_HIGH), d.get(REG_SYSTEM_PROG_V_MID), d.get(REG_SYSTEM_PROG_V_LOW))),
        SystemairDiagnosticText(coord, name, "Systemair Bootloader Version", lambda d: _fmt_ver(d.get(REG_SYSTEM_BOOT_PROG_V_HIGH), d.get(REG_SYSTEM_BOOT_PROG_V_MID), d.get(REG_SYSTEM_BOOT_PROG_V_LOW))),
        SystemairDiagnosticText(coord, name, "Systemair Program State", _prog_state_text),
    ])

    async_add_entities(entities)


class SystemairRegisterSensor(SystemairEntity, SensorEntity):
    should_poll = False

    def __init__(self, coordinator, name, desc: SensorDesc):
        SystemairEntity.__init__(self, coordinator, name)
        self._desc = desc
        self._attr_unique_id = f"systemair_{desc.reg}"
        self._attr_name = desc.name
        if desc.unit:
            self._attr_native_unit_of_measurement = desc.unit
        if desc.device_class:
            self._attr_device_class = desc.device_class

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    def _handle_coordinator_update(self):
        raw = self.coordinator.data.get(self._desc.reg)
        if raw is not None:
            val = raw
            if self._desc.scale is not None:
                val = round(raw * self._desc.scale, 1)
            # Sentinel for invalid temp (~ -40°C)
            if self._desc.device_class == SensorDeviceClass.TEMPERATURE and isinstance(val,
                                                                                       (int, float)) and val <= -30:
                self._attr_native_value = None
            else:
                self._attr_native_value = val
        self.async_write_ha_state()

class SystemairRotorStateText(SystemairEntity, SensorEntity):
    should_poll = False

    def __init__(self, coordinator, name):
        SystemairEntity.__init__(self, coordinator, name)
        self._attr_unique_id = "systemair_rotor_state"
        self._attr_name = "Systemair Rotor State"
        self._attr_native_value = None

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    def _handle_coordinator_update(self):
        raw = self.coordinator.data.get(REG_ROTOR_STATE)
        if raw is None:
            return
        self._attr_native_value = ROTOR_STATE_MAP.get(int(raw), "Unknown")
        self.async_write_ha_state()


def _fmt_ver(h, m, l):
    if None in (h, m, l):
        return None
    try:
        return f"{int(h)}.{int(m)}.{int(l)}"
    except (TypeError, ValueError):
        return None


def _prog_state_text(data: dict[int, int]):
    val = data.get(REG_SYSTEM_PROG_STATE)
    mapping = {1: "Main program", 2: "Boot loader", 3: "Boot loading"}
    try:
        return mapping.get(int(val)) if val is not None else None
    except (TypeError, ValueError):
        return None


class _DiagBase(SystemairEntity, SensorEntity):
    should_poll = False
    _attr_entity_category = EntityCategory.DIAGNOSTIC
    _attr_entity_registry_enabled_default = False

    def __init__(self, coordinator, name, unique_suffix: str):
        SystemairEntity.__init__(self, coordinator, name)
        self._unique_suffix = unique_suffix

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    def _handle_coordinator_update(self):
        # implemented by subclasses
        raise NotImplementedError


class SystemairDiagnosticNumber(_DiagBase):
    def __init__(self, coordinator, name, sensor_name: str, reg: int):
        super().__init__(coordinator, name, f"diag_{reg}")
        self._attr_unique_id = f"systemair_{self._unique_suffix}"
        self._attr_name = sensor_name
        self._reg = reg

    def _handle_coordinator_update(self):
        self._attr_native_value = self.coordinator.data.get(self._reg)
        self.async_write_ha_state()


class SystemairDiagnosticText(_DiagBase):
    def __init__(self, coordinator, name, sensor_name: str, compute_fn):
        super().__init__(coordinator, name, sensor_name.lower().replace(" ", "_"))
        self._attr_unique_id = f"systemair_{self._unique_suffix}"
        self._attr_name = sensor_name
        self._compute_fn = compute_fn
        self._attr_native_value = None

    def _handle_coordinator_update(self):
        try:
            self._attr_native_value = self._compute_fn(self.coordinator.data)
        except Exception:
            self._attr_native_value = None
        self.async_write_ha_state()