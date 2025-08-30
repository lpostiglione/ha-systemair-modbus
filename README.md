# Systemair Home Assistant Integration

The Systemair integration is used to integrate Home Assistant with ventilation units from [Systemair](https://www.systemair.com). Systemair designs and manufactures residential and commercial ventilation products, including heat recovery units like the VSR series. This integration focuses on local Modbus communication with a Systemair unit to monitor and control key parameters such as temperatures, fans, and rotor state.

Features at a glance:
- Read supply, extract, outdoor, and protection temperatures
- Monitor fan RPM and filter status
- Expose rotor state in a user-friendly format
- Provide diagnostic information (disabled by default)

For technical details about the unit’s Modbus registers used by this integration, see docs/modbus_registers.md.

Note: This is a community integration and is not affiliated with or endorsed by Systemair.
