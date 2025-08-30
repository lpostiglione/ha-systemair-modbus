from __future__ import annotations
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import Platform
from homeassistant.exceptions import ConfigEntryNotReady

from .const import (
    DOMAIN, DEFAULT_NAME,
    CONF_HOST, CONF_PORT, CONF_UNIT_ID, CONF_SCAN_INTERVAL,
    DEFAULT_SCAN_INTERVAL,
)
from .coordinator import SystemairCoordinator

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

    try:
        await coordinator.async_config_entry_first_refresh()
    except Exception as err:  # Coordinator will wrap modbus exceptions
        raise ConfigEntryNotReady from err

    entry.runtime_data = {
        "name": entry.title or DEFAULT_NAME,
        "coordinator": coordinator,
        "unit": unit,
    }

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    return unload_ok
