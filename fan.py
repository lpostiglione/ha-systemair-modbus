from __future__ import annotations
from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback

from .const import DOMAIN, REG_FAN_SPEED_LEVEL

PRESETS = ["Off", "Low", "Medium", "High"]
LEVEL_MAP = {"Off":0, "Low":1, "Medium":2, "High":3}
INV_LEVEL = {v:k for k,v in LEVEL_MAP.items()}

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coord = data["coordinator"]
    name = data["name"]
    async_add_entities([SystemairFan(coord, name)])

class SystemairFan(FanEntity):
    _attr_supported_features = FanEntityFeature.PRESET_MODE
    _attr_preset_modes = PRESETS

    def __init__(self, coordinator, name):
        self.coordinator = coordinator
        self._attr_unique_id = "systemair_fan"
        self._attr_name = f"{name} Fan"
        self._attr_device_info = DeviceInfo(
            identifiers={(DOMAIN, "systemair_vsr150")},
            name=name,
            manufacturer="Systemair",
            model="VSR150",
        )
        self._preset = "off"

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self):
        value = self.coordinator.data.get(REG_FAN_SPEED_LEVEL)
        if value is not None:
            self._preset = INV_LEVEL.get(int(value), "off")
            self._attr_is_on = int(value) > 0
        self.async_write_ha_state()

    @property
    def preset_mode(self):
        return self._preset

    async def async_set_preset_mode(self, preset_mode: str):
        value = LEVEL_MAP[preset_mode]
        await self.coordinator.async_write_register(REG_FAN_SPEED_LEVEL, value)
        await self.coordinator.async_request_refresh()

    async def async_turn_on(self, **kwargs):
        await self.async_set_preset_mode("low")

    async def async_turn_off(self, **kwargs):
        await self.async_set_preset_mode("off")
