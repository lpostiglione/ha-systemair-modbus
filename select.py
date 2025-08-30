from __future__ import annotations
from homeassistant.components.select import SelectEntity
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, REG_HC_TEMP_LVL, REG_SYSTEM_TYPE, REG_SYSTEM_PROG_V_HIGH, REG_SYSTEM_PROG_V_MID, REG_SYSTEM_PROG_V_LOW, SYSTEM_TYPE_MAP

OPTIONS = ["Off", "15 °C", "16 °C", "17 °C", "18 °C", "19 °C"]
LEVELS = {"Off":0, "15 °C":1, "16 °C":2, "17 °C":3, "18 °C":4, "19 °C":5}
INV_LEVELS = {v:k for k,v in LEVELS.items()}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coord = data["coordinator"]
    name = data["name"]
    async_add_entities([SystemairHeatingLevel(coord, name)])

class SystemairHeatingLevel(SelectEntity):
    _attr_options = OPTIONS

    def __init__(self, coordinator, name):
        self.coordinator = coordinator
        self._attr_unique_id = "systemair_heating_level"
        self._attr_name = f"{name} Heating Level"
        self._name = name
        self._attr_current_option = "Off"

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    @property
    def device_info(self) -> DeviceInfo:
        model_code = self.coordinator.data.get(REG_SYSTEM_TYPE)
        model = SYSTEM_TYPE_MAP.get(int(model_code)) if model_code is not None else None
        fw_h = self.coordinator.data.get(REG_SYSTEM_PROG_V_HIGH)
        fw_m = self.coordinator.data.get(REG_SYSTEM_PROG_V_MID)
        fw_l = self.coordinator.data.get(REG_SYSTEM_PROG_V_LOW)
        sw_version = None
        if None not in (fw_h, fw_m, fw_l):
            sw_version = f"{int(fw_h)}.{int(fw_m)}.{int(fw_l)}"
        return DeviceInfo(
            identifiers={(DOMAIN, "systemair")},
            name=self._name,
            manufacturer="Systemair",
            model=model or "Unknown",
            sw_version=sw_version,
        )

    def _handle_coordinator_update(self):
        val = self.coordinator.data.get(REG_HC_TEMP_LVL)
        if val is not None:
            self._attr_current_option = INV_LEVELS.get(int(val), "Off")
        self.async_write_ha_state()

    async def async_select_option(self, option: str):
        level = LEVELS[option]
        await self.coordinator.async_write_register(REG_HC_TEMP_LVL, level)
        await self.coordinator.async_request_refresh()
