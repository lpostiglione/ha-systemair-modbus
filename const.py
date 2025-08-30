DOMAIN = "systemair"
DEFAULT_NAME = "Systemair Ventilation"
CONF_HOST = "host"
CONF_PORT = "port"
CONF_UNIT_ID = "unit_id"
CONF_SCAN_INTERVAL = "scan_interval"
# Registers (Systemair D24810)
REG_FAN_SPEED_LEVEL = 101  # 0 Off, 1 Low, 2 Medium, 3 High
REG_FAN_SF_RPM = 111
REG_FAN_EF_RPM = 112

REG_HC_TEMP_LVL = 207  # 0 Off/Summer, 1..5 levels
REG_HC_TEMP_SP = 208  # readback °C (plain)

REG_HC_TEMP_IN1 = 214  # Supply (x10 °C)
REG_HC_TEMP_IN2 = 215  # Extract (x10 °C)
REG_HC_TEMP_IN4 = 217  # Overheat/Frost (x10 °C)
REG_HC_TEMP_IN5 = 218  # Outdoor (x10 °C)

REG_ROTOR_STATE = 351  # 0..11

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
