from __future__ import annotations
from typing import Optional
import math

from homeassistant.components.fan import FanEntity, FanEntityFeature
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.util.percentage import (
    ranged_value_to_percentage,
    percentage_to_ranged_value,
)
from homeassistant.util.scaling import int_states_in_range

from .const import DOMAIN, REG_FAN_SPEED_LEVEL
from .entity import SystemairEntity

# Device supports 3 discrete speeds (1..3). Off (0) is intentionally not supported.
SPEED_RANGE = (1, 3)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = hass.data[DOMAIN][entry.entry_id]
    coord = data["coordinator"]
    name = data["name"]
    entry_id = entry.entry_id
    async_add_entities([SystemairFan(coord, name, entry_id)])


class SystemairFan(SystemairEntity, FanEntity):
    def __init__(self, coordinator, name, entry_id: str):
        SystemairEntity.__init__(self, coordinator, name, entry_id)
        self._attr_unique_id = f"systemair_{entry_id}_fan"
        self._attr_has_entity_name = True
        self._attr_is_on = True  # Off is not supported by design
        self._percentage: Optional[int] = None

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self):
        value = self.coordinator.data.get(REG_FAN_SPEED_LEVEL)
        if value is not None:
            # Coerce to supported range; if device reports 0, treat as 1
            try:
                val = int(value)
            except (TypeError, ValueError):
                val = 1
            if val < SPEED_RANGE[0]:
                val = SPEED_RANGE[0]
            if val > SPEED_RANGE[1]:
                val = SPEED_RANGE[1]
            self._percentage = ranged_value_to_percentage(SPEED_RANGE, val)
            self._attr_is_on = True  # remain on; we don't expose off
        self.async_write_ha_state()

    @property
    def supported_features(self) -> FanEntityFeature:
        return FanEntityFeature.SET_SPEED

    @property
    def percentage(self) -> Optional[int]:
        return self._percentage

    async def async_set_percentage(self, percentage: int) -> None:
        # Map percentage to one of 1..3 discrete levels, ceiling to avoid 0
        value_in_range = percentage_to_ranged_value(SPEED_RANGE, percentage)
        value = int(math.ceil(value_in_range))
        if value < SPEED_RANGE[0]:
            value = SPEED_RANGE[0]
        if value > SPEED_RANGE[1]:
            value = SPEED_RANGE[1]
        await self.coordinator.async_write_register(REG_FAN_SPEED_LEVEL, value)
        await self.coordinator.async_request_refresh()

    @property
    def speed_count(self) -> int:
        return int_states_in_range(SPEED_RANGE)
