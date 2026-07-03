from unittest.mock import MagicMock

from homeassistant.components.fan import FanEntityFeature

from systemair.fan import SystemairFan


async def test_fan_declares_turn_on_off_features():
    fan = SystemairFan(MagicMock(), "Test", "test_entry")
    assert fan.supported_features & FanEntityFeature.SET_SPEED
    assert fan.supported_features & FanEntityFeature.TURN_ON
    assert fan.supported_features & FanEntityFeature.TURN_OFF
