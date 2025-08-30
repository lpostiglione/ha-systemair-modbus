from __future__ import annotations
from homeassistant.helpers.entity import DeviceInfo

from .const import (
    DOMAIN,
    REG_SYSTEM_TYPE, REG_SYSTEM_PROG_V_HIGH, REG_SYSTEM_PROG_V_MID, REG_SYSTEM_PROG_V_LOW,
    SYSTEM_TYPE_MAP,
)


class SystemairEntity:
    """Base entity for Systemair integration.

    Provides shared device information based on coordinator data.
    """

    def __init__(self, coordinator, name: str) -> None:
        self.coordinator = coordinator
        self._name = name

    @property
    def device_info(self) -> DeviceInfo:
        model_code = self.coordinator.data.get(REG_SYSTEM_TYPE)
        model = SYSTEM_TYPE_MAP.get(int(model_code)) if model_code is not None else None
        fw_h = self.coordinator.data.get(REG_SYSTEM_PROG_V_HIGH)
        fw_m = self.coordinator.data.get(REG_SYSTEM_PROG_V_MID)
        fw_l = self.coordinator.data.get(REG_SYSTEM_PROG_V_LOW)
        sw_version = None
        if None not in (fw_h, fw_m, fw_l):
            try:
                sw_version = f"{int(fw_h)}.{int(fw_m)}.{int(fw_l)}"
            except (TypeError, ValueError):
                sw_version = None
        return DeviceInfo(
            identifiers={(DOMAIN, "systemair")},
            name=self._name,
            manufacturer="Systemair",
            model=model or "Unknown",
            sw_version=sw_version,
        )
