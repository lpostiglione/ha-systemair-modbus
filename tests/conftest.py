"""Shared fixtures for the Systemair integration tests.

The integration lives at the repository root (content_in_root), so the repo's
parent directory is added to sys.path to make ``import systemair`` work.
"""
import sys
from pathlib import Path
from unittest.mock import AsyncMock, patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT.parent) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT.parent))

from pytest_homeassistant_custom_component.common import (  # noqa: E402
    MockModule,
    mock_integration,
    mock_platform,
)

from systemair import config_flow as systemair_config_flow  # noqa: E402
from systemair.const import DOMAIN  # noqa: E402


@pytest.fixture(autouse=True)
def mock_systemair_integration(hass):
    """Register the systemair integration and its config flow with the loader."""
    mock_integration(
        hass,
        MockModule(
            domain=DOMAIN,
            async_setup_entry=AsyncMock(return_value=True),
            async_unload_entry=AsyncMock(return_value=True),
        ),
    )
    mock_platform(hass, f"{DOMAIN}.config_flow", systemair_config_flow)


@pytest.fixture(autouse=True)
def mock_modbus_connection():
    """Avoid real Modbus TCP connections during config flow tests."""
    with patch.object(systemair_config_flow, "_test_connection", return_value=True):
        yield
