# Systemair Home Assistant Integration

The Systemair integration is used to integrate Home Assistant with ventilation units from [Systemair](https://www.systemair.com). Systemair designs and manufactures residential and commercial ventilation products, including heat recovery units like the VSR series. This integration focuses on local Modbus communication with a Systemair unit to monitor and control key parameters such as temperatures, fans, and rotor state.

Features at a glance:
- Read supply, extract, outdoor, and protection temperatures
- Monitor fan RPM and filter status
- Expose rotor state in a user-friendly format
- Provide diagnostic information (disabled by default)

For technical details about the unit’s Modbus registers used by this integration, see docs/modbus_registers.md.

Note: This is a community integration and is not affiliated with or endorsed by Systemair.

## Prerequisites

- Home Assistant 2025.8.3 or newer.
- A compatible Systemair ventilation unit (e.g., VSR/VTR/VTC series) with a Modbus interface available on your network.
- IP address/hostname of the Modbus TCP interface, TCP port (default 502), and Modbus unit ID (default 1).
- Network connectivity between Home Assistant and the Systemair device.

## Installation

Using HACS (recommended):
- In Home Assistant, go to HACS > Integrations.
- Click the three dots (⋮) in the top-right and select "Custom repositories".
- Add this repository URL as type "Integration".
- Search for "Systemair" in HACS > Integrations and install it.
- Restart Home Assistant when prompted.

Manual installation:
- Download the latest release ZIP of this repository.
- Extract it and copy the folder named "systemair" into your Home Assistant config directory under `custom_components/systemair`.
  - Final path should be `<config>/custom_components/systemair/` containing `__init__.py`, `manifest.json`, etc.
- Restart Home Assistant.

## Configuration

- In Home Assistant, go to Settings > Devices & Services.
- Click "Add Integration" and search for "Systemair".
- Enter the required connection details when prompted:
  - Host (IP or hostname)
  - Port (optional, default 502)
  - Unit ID (optional, default 1)
  - Scan interval in seconds (optional, default 10)
- Submit to create the integration entry.
- You can later adjust the scan interval from the integration's Options.

For technical details about the unit’s Modbus registers used by this integration, see docs/modbus_registers.md.
