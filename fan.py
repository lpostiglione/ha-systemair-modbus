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

from .const import DOMAIN, REG_FAN_SPEED_LEVEL, REG_FAN_ALLOW_MANUAL_FAN_STOP
from .entity import SystemairEntity

# Device supports 3 discrete speeds for on-state (1..3). Off (0) is supported when manual stop is allowed.
SPEED_RANGE = (1, 3)


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    data = entry.runtime_data
    coord = data["coordinator"]
    name = data["name"]
    entry_id = entry.entry_id
    async_add_entities([SystemairFan(coord, name, entry_id)])


class SystemairFan(SystemairEntity, FanEntity):
    def __init__(self, coordinator, name, entry_id: str):
        SystemairEntity.__init__(self, coordinator, name, entry_id)
        self._attr_unique_id = f"systemair_{entry_id}_fan"
        self._attr_has_entity_name = True
        self._attr_name = "Fan"
        self._attr_is_on = None  # Unknown until first update
        self._percentage: Optional[int] = None

    async def async_added_to_hass(self):
        self.async_on_remove(self.coordinator.async_add_listener(self._handle_coordinator_update))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self):
        value = self.coordinator.data.get(REG_FAN_SPEED_LEVEL)
        if value is not None:
            # Map device value to HA state; 0 = off, 1..3 = discrete speeds
            try:
                val = int(value)
            except (TypeError, ValueError):
                val = 0
            if val <= 0:
                self._percentage = 0
                self._attr_is_on = False
            else:
                if val < SPEED_RANGE[0]:
                    val = SPEED_RANGE[0]
                if val > SPEED_RANGE[1]:
                    val = SPEED_RANGE[1]
                self._percentage = ranged_value_to_percentage(SPEED_RANGE, val)
                self._attr_is_on = True
        self.async_write_ha_state()

    @property
    def supported_features(self) -> FanEntityFeature:
        return FanEntityFeature.SET_SPEED

    @property
    def percentage(self) -> Optional[int]:
        return self._percentage

    async def async_set_percentage(self, percentage: int) -> None:
        if percentage is None or percentage <= 0:
            await self.async_turn_off()
            return
        # Map percentage to one of 1..3 discrete levels, ceiling to avoid 0
        value_in_range = percentage_to_ranged_value(SPEED_RANGE, percentage)
        value = int(math.ceil(value_in_range))
        if value < SPEED_RANGE[0]:
            value = SPEED_RANGE[0]
        if value > SPEED_RANGE[1]:
            value = SPEED_RANGE[1]
        await self.coordinator.async_write_register(REG_FAN_SPEED_LEVEL, value)
        await self.coordinator.async_request_refresh()

    async def async_turn_off(self, **kwargs) -> None:
        allow = self.coordinator.data.get(REG_FAN_ALLOW_MANUAL_FAN_STOP)
        # If manual stop allowed, write 0; otherwise, fall back to Low (1)
        value = 0 if allow == 1 else 1
        await self.coordinator.async_write_register(REG_FAN_SPEED_LEVEL, value)
        await self.coordinator.async_request_refresh()

    async def async_turn_on(self, percentage: Optional[int] = None, **kwargs) -> None:
        # If a specific percentage is provided, use it; otherwise default to Low if unknown
        if percentage is None:
            percentage = self._percentage or ranged_value_to_percentage(SPEED_RANGE, SPEED_RANGE[0])
        await self.async_set_percentage(percentage)

    @property
    def speed_count(self) -> int:
        return int_states_in_range(SPEED_RANGE)
