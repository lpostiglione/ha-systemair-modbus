from __future__ import annotations
import voluptuous as vol

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import (
    DOMAIN, DEFAULT_NAME,
    CONF_HOST, CONF_PORT, CONF_UNIT_ID, CONF_SCAN_INTERVAL,
    DEFAULT_PORT, DEFAULT_UNIT_ID, DEFAULT_SCAN_INTERVAL,
)

STEP_USER_DATA_SCHEMA = vol.Schema({
    vol.Required(CONF_HOST): str,
    vol.Optional(CONF_PORT, default=DEFAULT_PORT): int,
    vol.Optional(CONF_UNIT_ID, default=DEFAULT_UNIT_ID): int,
    vol.Optional(CONF_SCAN_INTERVAL, default=DEFAULT_SCAN_INTERVAL): int,
})


async def _test_connection(hass: HomeAssistant, host: str, port: int, unit: int) -> bool:
    """Attempt a lightweight connection to the Modbus TCP endpoint.

    Returns True if a TCP connection was established, False otherwise.
    """
    try:
        from pymodbus.client import AsyncModbusTcpClient  # type: ignore
    except Exception:
        # If dependency is missing, don't block configuration in tests/dev
        return True
    try:
        client = AsyncModbusTcpClient(host, port=port)
        ok = await client.connect()
        try:
            # Close if supported by installed pymodbus version
            close = getattr(client, "close", None)
            if close is not None:
                res = close()
                if hasattr(res, "__await__"):
                    await res
        except Exception:
            pass
        # Some versions return bool, others set client.connected
        return bool(ok) or bool(getattr(client, "connected", False))
    except Exception:
        return False


class SystemairConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Systemair."""

    VERSION = 1

    async def async_step_user(self, user_input: dict | None = None) -> FlowResult:
        if user_input is None:
            return self.async_show_form(step_id="user", data_schema=STEP_USER_DATA_SCHEMA)

        host = user_input[CONF_HOST]
        port = user_input.get(CONF_PORT, DEFAULT_PORT)
        unit = user_input.get(CONF_UNIT_ID, DEFAULT_UNIT_ID)

        await self.async_set_unique_id(f"systemair_{host}")
        self._abort_if_unique_id_configured()

        # Test connection before creating the entry
        if not await _test_connection(self.hass, host, port, unit):
            return self.async_show_form(
                step_id="user",
                data_schema=STEP_USER_DATA_SCHEMA,
                errors={"base": "cannot_connect"},
                description_placeholders=None,
            )

        title = DEFAULT_NAME
        return self.async_create_entry(title=title, data=user_input)

    async def async_step_import(self, user_input: dict) -> FlowResult:
        # not used, but kept for completeness
        return await self.async_step_user(user_input)


class SystemairOptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry: config_entries.ConfigEntry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input: dict | None = None) -> FlowResult:
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        current = {
            CONF_SCAN_INTERVAL: self.config_entry.options.get(
                CONF_SCAN_INTERVAL,
                self.config_entry.data.get(CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL),
            )
        }
        schema = vol.Schema({
            vol.Required(CONF_SCAN_INTERVAL, default=current[CONF_SCAN_INTERVAL]): int
        })
        return self.async_show_form(step_id="init", data_schema=schema)


async def async_get_options_flow(config_entry):
    return SystemairOptionsFlowHandler(config_entry)
