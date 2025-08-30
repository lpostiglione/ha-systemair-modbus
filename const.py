DOMAIN = "systemair"
DEFAULT_NAME = "Systemair Ventilation"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_UNIT_ID = "unit_id"
CONF_SCAN_INTERVAL = "scan_interval"
# Registers (Systemair D24810)
REG_FAN_SPEED_LEVEL = 101  # 0 Off, 1 Low, 2 Medium, 3 High
REG_FAN_SF_PWM = 109  # 0..100 % (0-10V)
REG_FAN_EF_PWM = 110  # 0..100 % (0-10V)
REG_FAN_SF_RPM = 111
REG_FAN_EF_RPM = 112

# Heating/Cooling
REG_HC_HEATER_TYPE = 201  # 0: No heater, 1: Water, 2: Electrical, 3: Other
REG_HC_COOLER_TYPE = 202  # 0: No cooler, 1: Water cooler
REG_HC_WC_SIGNAL = 204    # Cooler output (%)
REG_HC_WH_SIGNAL = 205    # Analog heater output (%)
REG_HC_TEMP_LVL = 207  # 0 Off/Summer, 1..5 levels
REG_HC_TEMP_SP = 208  # readback °C (plain)

REG_HC_TEMP_IN1 = 214  # Supply (x10 °C)
REG_HC_TEMP_IN2 = 215  # Extract (x10 °C)
REG_HC_TEMP_IN3 = 216  # Exhaust/Preheater (x10 °C)
REG_HC_TEMP_IN4 = 217  # Overheat/Frost (x10 °C)
REG_HC_TEMP_IN5 = 218  # Outdoor (x10 °C)
REG_HC_PREHEATER_TYPE = 220  # 0: No preheater, 1: Electrical preheater

# Rotor / Damper
REG_ROTOR_STATE = 351  # 0..11
REG_DAMPER_PWM = 301   # 0..100 % (0-10V)

# RH sensor
REG_RH_SENSOR_VALUE = 381
REG_RH_SENSOR_DATA_VALID = 383  # 1 if valid data available
REG_RH_SENSOR_PRESENT = 655  # 0 Not used, 1 Connected and used

# Filter
REG_FILTER_PER = 601  # months
REG_FILTER_DAYS = 602  # days

# System parameters (501+)
REG_SYSTEM_TYPE = 501
REG_SYSTEM_PROG_V_HIGH = 502
REG_SYSTEM_PROG_V_MID = 503
REG_SYSTEM_PROG_V_LOW = 504
REG_SYSTEM_BOOT_PROG_V_HIGH = 505
REG_SYSTEM_BOOT_PROG_V_MID = 506
REG_SYSTEM_BOOT_PROG_V_LOW = 507
REG_SYSTEM_PROG_STATE = 508

SYSTEM_TYPE_MAP = {
    0: "VR400",
    1: "VR700",
    2: "VR700DK",
    3: "VR400DE",
    4: "VTC300",
    5: "VTC700",
    12: "VTR150K",
    13: "VTR200B",
    14: "VSR300",
    15: "VSR500",
    16: "VSR150",
    17: "VTR300",
    18: "VTR500",
    19: "VSR300DE",
    20: "VTC200",
    21: "VTC100",
}

SCALE_TENTH = 0.1
# Persist settings to non-volatile memory
REG_STORE_NVM = 549            # write 165 to commit to NVM

# Friendly rotor state mapping (REG_ROTOR_STATE = 351)
ROTOR_STATE_MAP = {
    0: "Normal",
    1: "Rotor fault assumed",
    2: "Rotor fault detected",
    3: "Summer cond. valid (not active)",
    4: "Summer mode",
    5: "Waiting to exit Manual summer",
    6: "Manual summer mode",
    7: "Rotor cleaning (summer mode)",
    8: "Rotor cleaning (manual summer)",
    9: "Fans off",
    10: "Rotor cleaning (fans off)",
    11: "Rotor fault — conditions not valid",
}

DEFAULT_PORT = 502
DEFAULT_UNIT_ID = 1
DEFAULT_SCAN_INTERVAL = 10  # seconds
