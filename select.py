from __future__ import annotations
from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DOMAIN, REG_HC_TEMP_LVL
from .entity import SystemairEntity

OPTIONS = ["Off", "15 °C", "16 °C", "17 °C", "18 °C", "19 °C"]
LEVELS = {"Off":0, "15 °C":1, "16 °C":2, "17 °C":3, "18 °C":4, "19 °C":5}
INV_LEVELS = {v:k for k,v in LEVELS.items()}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coord = data["coordinator"]
    name = data["name"]
    entry_id = entry.entry_id
    async_add_entities([SystemairHeatingLevel(coord, name, entry_id)])

class SystemairHeatingLevel(SystemairEntity, SelectEntity):
    _attr_options = OPTIONS

    def __init__(self, coordinator, name, entry_id: str):
        SystemairEntity.__init__(self, coordinator, name, entry_id)
        self._attr_unique_id = f"systemair_{entry_id}_heating_level"
        self._attr_name = f"{name} Heating Level"
        self._attr_current_option = "Off"

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    def _handle_coordinator_update(self):
        val = self.coordinator.data.get(REG_HC_TEMP_LVL)
        if val is not None:
            self._attr_current_option = INV_LEVELS.get(int(val), "Off")
        self.async_write_ha_state()

    async def async_select_option(self, option: str):
        level = LEVELS[option]
        await self.coordinator.async_write_register(REG_HC_TEMP_LVL, level)
        await self.coordinator.async_request_refresh()
