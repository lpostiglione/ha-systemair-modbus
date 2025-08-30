import pytest
from homeassistant.const import CONF_HOST
from homeassistant.data_entry_flow import FlowResultType

from systemair.const import DOMAIN


@pytest.mark.asyncio
async def test_import_flow(hass):
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": "import"},
        data={CONF_HOST: "5.6.7.8"},
    )
    assert result["type"] == FlowResultType.CREATE_ENTRY
    assert result["data"][CONF_HOST] == "5.6.7.8"
