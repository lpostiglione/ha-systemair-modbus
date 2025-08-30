import pytest
from homeassistant.const import CONF_HOST
from homeassistant.data_entry_flow import FlowResultType
from homeassistant.config_entries import SOURCE_USER

from systemair.const import DOMAIN


@pytest.mark.asyncio
async def test_user_flow_minimal(hass):
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": SOURCE_USER},
    )
    assert result["type"] == FlowResultType.FORM
    assert result["step_id"] == "user"

    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_HOST: "10.0.0.10"},
    )

    assert result2["type"] == FlowResultType.CREATE_ENTRY
    assert result2["title"]
    assert result2["data"][CONF_HOST] == "10.0.0.10"


@pytest.mark.asyncio
async def test_unique_id_enforced(hass):
    # First add entry
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": SOURCE_USER},
    )
    result = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {CONF_HOST: "192.168.1.2"},
    )
    assert result["type"] == FlowResultType.CREATE_ENTRY

    # Second attempt with same host should abort due to unique ID
    result2 = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": SOURCE_USER},
    )
    # form shown
    assert result2["type"] == FlowResultType.FORM

    result3 = await hass.config_entries.flow.async_configure(
        result2["flow_id"],
        {CONF_HOST: "192.168.1.2"},
    )
    assert result3["type"] == FlowResultType.ABORT
    assert result3["reason"] == "already_configured"
