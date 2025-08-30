from __future__ import annotations
from typing import Any

from homeassistant.components.diagnostics import async_redact_data
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import (
    CONF_HOST,
)

# Redact potentially sensitive connection details
TO_REDACT: set[str] = {CONF_HOST}


async def async_get_config_entry_diagnostics(
    hass: HomeAssistant, entry: ConfigEntry
) -> dict[str, Any]:
    """Return diagnostics for a config entry.

    Exposes the config entry data/options (with sensitive fields redacted) and
    current coordinator state including the raw register cache.
    """
    runtime = getattr(entry, "runtime_data", {})
    coordinator = None
    unit: int | None = None

    if isinstance(runtime, dict):
        coordinator = runtime.get("coordinator")
        unit = runtime.get("unit")

    registers: dict[int, int] | None = None
    update_interval_seconds: float | None = None
    last_update_success: bool | None = None

    if coordinator is not None:
        # coordinator.data is a dict[int, int] of raw register values
        registers = getattr(coordinator, "data", None)
        try:
            ui = getattr(coordinator, "update_interval", None)
            if ui is not None:
                update_interval_seconds = float(ui.total_seconds())  # type: ignore[call-arg]
        except Exception:
            update_interval_seconds = None
        last_update_success = getattr(coordinator, "last_update_success", None)

    return {
        "entry_data": async_redact_data(entry.data, TO_REDACT),
        "entry_options": async_redact_data(entry.options, TO_REDACT),
        "coordinator": {
            "unit": unit,
            "update_interval_seconds": update_interval_seconds,
            "last_update_success": last_update_success,
        }
        if coordinator is not None
        else None,
        "registers": registers,
    }
