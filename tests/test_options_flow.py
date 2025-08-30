import pytest
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.config_entries import SOURCE_USER
from homeassistant.const import CONF_HOST

from systemair.const import DOMAIN, CONF_SCAN_INTERVAL, DEFAULT_SCAN_INTERVAL


@pytest.mark.asyncio
async def test_options_flow_change_interval(hass):
    # Create initial entry via flow
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": SOURCE_USER}
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"], {CONF_HOST: "1.2.3.4"}
    )
    entry = result["result"]

    # Start options flow
    result2 = await hass.config_entries.options.async_init(entry.entry_id)
    assert result2["type"] == FlowResultType.FORM
    assert result2["step_id"] == "init"

    # Submit with new scan interval
    result3 = await hass.config_entries.options.async_configure(
        result2["flow_id"], {CONF_SCAN_INTERVAL: DEFAULT_SCAN_INTERVAL + 5}
    )
    assert result3["type"] == FlowResultType.CREATE_ENTRY
    assert result3["data"][CONF_SCAN_INTERVAL] == DEFAULT_SCAN_INTERVAL + 5
