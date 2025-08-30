# Modbus Registers Reference (from *Modbus for Residential units – User Manual D24810-EN_GB, 2017-02-10*)

_Columns: Name, Address, R/W, NVM, Scaling, Access (Reg/Coil), Description/Remarks._

_Legend: **Y¹** values are persisted after writing 165 to REG_STORE_NVM (549). **N** under NVM means not stored; blank
means not specified._

## 7.1 Registers for Fan Control

| Name                          | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                         |
|-------------------------------|---------|-----|-----|---------|-------------------|---------------------------------------------------------------------------------------------|
| REG_FAN_SPEED_LEVEL           | 101     | R/W | Y¹  |         | Reg               | 0: Off, 1: Low, 2: Normal, 3: High, 4: Auto                                                 |
| REG_FAN_SF_FLOW_LOW           | 102     | R/W | Y¹  |         | Reg               | Supply air fan speed for low speed                                                          |
| REG_FAN_EF_FLOW_LOW           | 103     | R/W | Y¹  |         | Reg               | Extract air fan speed for low speed                                                         |
| REG_FAN_SF_FLOW_NOM           | 104     | R/W | Y¹  |         | Reg               | Supply air fan speed for nominal speed                                                      |
| REG_FAN_EF_FLOW_NOM           | 105     | R/W | Y¹  |         | Reg               | Extract air fan speed for nominal speed                                                     |
| REG_FAN_SF_FLOW_HIGH          | 106     | R/W | Y¹  |         | Reg               | Supply air fan speed for high speed                                                         |
| REG_FAN_EF_FLOW_HIGH          | 107     | R/W | Y¹  |         | Reg               | Extract air fan speed for high speed                                                        |
| REG_FAN_FLOW_UNITS            | 108     | R/W | Y   |         | Reg               | 0: l/s, 1: m³/h                                                                             |
| REG_FAN_SF_PWM                | 109     | R   |     |         | Reg               | 0..100: 0–10V                                                                               |
| REG_FAN_EF_PWM                | 110     | R   |     |         | Reg               | 0..100: 0–10V                                                                               |
| REG_FAN_SF_RPM                | 111     | R   |     |         | Reg               | Rotations per minute                                                                        |
| REG_FAN_EF_RPM                | 112     | R   |     |         | Reg               | Rotations per minute                                                                        |
| REG_FAN_ALLOW_MANUAL_FAN_STOP | 114     | R/W | Y   |         | Reg + Coil (1809) | Manual fan stop allowed. 0: CD cannot set fan speed to off. 1: CD can set fan speed to off. |
| REG_FAN_SPEED_LOG_RESET       | 115     | W   | N   |         | Reg               | Write 90 to clear REG_FAN_SPEED_LOG_xF_LVLx values.                                         |
| REG_FAN_SPEED_LOG_SF_LVL1     | 116     | R   |     |         | Reg               | Fan speed log values for supply fan, level 1.                                               |
| REG_FAN_SPEED_LOG_SF_LVL2     | 117     | R   |     |         | Reg               | Supply fan, level 2.                                                                        |
| REG_FAN_SPEED_LOG_SF_LVL3     | 118     | R   |     |         | Reg               | Supply fan, level 3.                                                                        |
| REG_FAN_SPEED_LOG_SF_LVL4     | 119     | R   |     |         | Reg               | Supply fan, level 4.                                                                        |
| REG_FAN_SPEED_LOG_SF_LVL5     | 120     | R   |     |         | Reg               | Supply fan, level 5.                                                                        |
| REG_FAN_SPEED_LOG_EF_LVL1     | 121     | R   |     |         | Reg               | Extract fan, level 1.                                                                       |
| REG_FAN_SPEED_LOG_EF_LVL2     | 122     | R   |     |         | Reg               | Extract fan, level 2.                                                                       |
| REG_FAN_SPEED_LOG_EF_LVL3     | 123     | R   |     |         | Reg               | Extract fan, level 3.                                                                       |
| REG_FAN_SPEED_LOG_EF_LVL4     | 124     | R   |     |         | Reg               | Extract fan, level 4.                                                                       |
| REG_FAN_SPEED_LOG_EF_LVL5     | 125     | R   |     |         | Reg               | Extract fan, level 5.                                                                       |
| REG_FAN_SPEED_LOG_SF_NR_LVL1  | 126     | R   |     |         | Reg               | Supply fan non-resettable, level 1.                                                         |
| REG_FAN_SPEED_LOG_SF_NR_LVL2  | 127     | R   |     |         | Reg               | Supply fan non-resettable, level 2.                                                         |
| REG_FAN_SPEED_LOG_SF_NR_LVL3  | 128     | R   |     |         | Reg               | Supply fan non-resettable, level 3.                                                         |
| REG_FAN_SPEED_LOG_SF_NR_LVL4  | 129     | R   |     |         | Reg               | Supply fan non-resettable, level 4.                                                         |
| REG_FAN_SPEED_LOG_SF_NR_LVL5  | 130     | R   |     |         | Reg               | Supply fan non-resettable, level 5.                                                         |
| REG_FAN_SPEED_LOG_EF_NR_LVL1  | 131     | R   |     |         | Reg               | Extract fan non-resettable, level 1.                                                        |
| REG_FAN_SPEED_LOG_EF_NR_LVL2  | 132     | R   |     |         | Reg               | Extract fan non-resettable, level 2.                                                        |
| REG_FAN_SPEED_LOG_EF_NR_LVL3  | 133     | R   |     |         | Reg               | Extract fan non-resettable, level 3.                                                        |
| REG_FAN_SPEED_LOG_EF_NR_LVL4  | 134     | R   |     |         | Reg               | Extract fan non-resettable, level 4.                                                        |
| REG_FAN_SPEED_LOG_EF_NR_LVL5  | 135     | R   |     |         | Reg               | Extract fan non-resettable, level 5.                                                        |
| REG_FAN_SYSTEM_CURVE_SF       | 136     | R/W | Y   |         | Reg               | System curve for supply fan (1–20).                                                         |
| REG_FAN_SYSTEM_CURVE_EF       | 137     | R/W | Y   |         | Reg               | System curve for extract fan (1–10).                                                        |
| REG_FAN_CONTROL_TYPE          | 138     | R/W |     |         | Reg               | 0: Air flow, 1: Speed.                                                                      |
| REG_FAN_INTERLOCK             | 139     | R   |     |         | Reg               | Interlock NO relay state: 0 off, 1 active.                                                  |

## 7.2 Registers for Heater Control

| Name                             | Address | R/W | NVM | Scaling | Access (Reg/Coil)       | Description/Remarks                                                                                         |
|----------------------------------|---------|-----|-----|---------|-------------------------|-------------------------------------------------------------------------------------------------------------|
| REG_HC_HEATER_TYPE               | 201     | R/W | Y¹  | 1       | Reg                     | 0: No heater, 1: Water heater, 2: Electrical heater, 3: Other                                               |
| REG_HC_COOLER_TYPE               | 202     | R/W | Y¹  | 1       | Reg                     | 0: No cooler, 1: Water cooler                                                                               |
| REG_HC_WC_SIGNAL                 | 204     | R   |     | 1       | Reg                     | Signal to cooler output (%)                                                                                 |
| REG_HC_WH_SIGNAL                 | 205     | R   |     | 1       | Reg                     | Signal to analog heater output (%)                                                                          |
| REG_HC_FPS_LEVEL                 | 206     | R/W | Y¹  | 1       | Reg                     | Frost protection level. Allowed values: 70,80,90,100,110,120 → 7,8,9,10,11,12 °C                            |
| REG_HC_TEMP_LVL                  | 207     | R/W | Y¹  |         | Reg                     | Temperature set point level. 0: Manual summer. 1–5: use REG_HC_TEMP_LVL1..5. 6–29: extension of levels 1–5. |
| REG_HC_TEMP_SP                   | 208     | R   |     | 1       | Reg                     | Temperature set point                                                                                       |
| REG_HC_TEMP_LVL1                 | 209     | R   |     | 10      | Reg                     | Temperature level 1 ×10. (Not supported from PCU‑ECx v5.01.00)                                              |
| REG_HC_TEMP_LVL2                 | 210     | R   |     | 10      | Reg                     | Temperature level 2 ×10. (Not supported from PCU‑ECx v5.01.00)                                              |
| REG_HC_TEMP_LVL3                 | 211     | R   |     | 10      | Reg                     | Temperature level 3 ×10. (Not supported from PCU‑ECx v5.01.00)                                              |
| REG_HC_TEMP_LVL4                 | 212     | R   |     | 10      | Reg                     | Temperature level 4 ×10. (Not supported from PCU‑ECx v5.01.00)                                              |
| REG_HC_TEMP_LVL5                 | 213     | R   |     | 10      | Reg                     | Temperature level 5 ×10. (Not supported from PCU‑ECx v5.01.00)                                              |
| REG_HC_TEMP_IN1                  | 214     | R   |     | 10      | Reg                     | Temperature sensor 1 ×10 (Supply air)                                                                       |
| REG_HC_TEMP_IN2                  | 215     | R   |     | 10      | Reg                     | Temperature sensor 2 ×10 (Extract air)                                                                      |
| REG_HC_TEMP_IN3                  | 216     | R   |     | 10      | Reg                     | Temperature sensor 3 ×10 (Exhaust/Preheater)                                                                |
| REG_HC_TEMP_IN4                  | 217     | R   |     | 10      | Reg                     | Temperature sensor 4 ×10 (Overheat/Frost protection)                                                        |
| REG_HC_TEMP_IN5                  | 218     | R   |     | 10      | Reg                     | Temperature sensor 5 ×10 (Outdoor air)                                                                      |
| REG_HC_TEMP_STATE                | 219     | R   |     | 1       | Reg + Coils (3489–3493) | Sensor fault flags per input 1..5. 0: no fault, 1: fault                                                    |
| REG_HC_PREHEATER_TYPE            | 220     | R/W | Y   |         | Reg                     | 0: No preheater, 1: Electrical preheater                                                                    |
| REG_HC_HEATER_TEMP_SP_HOME_LEAVE | 221     | R   |     |         | Reg                     | Set point support control heater during Home/Leave                                                          |
| REG_HC_TEMP_SP_DEG               | 222     | R/W |     |         | Reg                     | Setpoint for temperature regulation (×10)                                                                   |
| REG_HC_INTERVAL_COOLING_LOW      | 223     | R/W |     |         | Reg                     | Combined controller output at which cooling is at maximum                                                   |
| REG_HC_INTERVAL_COOLING_HIGH     | 224     | R/W |     |         | Reg                     | Combined controller output at which cooling is at minimum                                                   |
| REG_HC_INTERVAL_EXCHANGING_LOW   | 225     | R/W |     |         | Reg                     | Lower limit for heat exchanging range (combined regulator)                                                  |
| REG_HC_INTERVAL_EXCHANGING_HIGH  | 226     | R/W |     |         | Reg                     | Upper limit for heat exchanging range (combined regulator)                                                  |
| REG_HC_INTERVAL_HEATING_LOW      | 227     | R/W |     |         | Reg                     | Lower limit for heating range (combined regulator)                                                          |
| REG_HC_INTERVAL_HEATING_HIGH     | 228     | R/W |     |         | Reg                     | Upper limit for heating range (combined regulator)                                                          |
| REG_HC_P_BAND                    | 229     | R/W |     |         | Reg                     | P-Band for combined temperature regulator (×10). Range 10–600 = 1–60 °C                                     |
| REG_HC_I_TIME                    | 230     | R/W |     |         | Reg                     | I-Time for combined temperature regulator. 1–240; 0: no integration                                         |
| REG_PREHEATER_SETPOINT           | 231     | R/W |     |         | Reg                     | Preheater set point. Range −300–0 (= −30 to 0 °C)                                                           |
| REG_PREHEATER_P_BAND             | 232     | R/W |     |         | Reg                     | Preheater P-Band (×10). Range 10–600 (= 1–60 °C)                                                            |
| REG_PREHEATER_I_TIME             | 233     | R/W |     |         | Reg                     | Preheater I-Time. 1–240; 0: no integration                                                                  |
| REG_HC_OUT                       | 234     | R   |     |         | Reg                     | Output of split-level temperature controller (0–100%)                                                       |
| REG_PREHEATER_OUT                | 235     | R   |     |         | Reg                     | Output of PI controller for electrical preheater (0–100%)                                                   |
| REG_HC_TEMP_SP_DEG_STEP          | 236     | R   |     |         | Reg                     | Temperature setting step (×10). Ex: 10=1.0°C; 25=2.5°C                                                      |

## 7.3 Registers for the Damper

| Name           | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                       |
|----------------|---------|-----|-----|---------|-------------------|-------------------------------------------|
| REG_DAMPER_PWM | 301     | R   |     |         | Reg               | Output value for exchanger. 0–100 → 0–10V |

## 7.4 Registers for the Rotor

| Name                     | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                                                                                                                                                                                                                                             |
|--------------------------|---------|-----|-----|---------|-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG_ROTOR_STATE          | 351     | R   |     |         | Reg               | Rotor control state: 0 Normal, 1 Fault assumed, 2 Fault detected, 3 Summer cond. pending, 4 Summer mode, 5 Waiting exit manual summer (temp), 6 Manual summer, 7 Rotor cleaning (summer), 8 Rotor cleaning (manual summer), 9 Fans off, 10 Rotor cleaning (fans off), 11 Rotor fault conditions no longer valid |
| REG_ROTOR_RELAY_ACTIVE   | 352     | R   |     |         | Reg + Coil (5617) | Rotor relay active. 0: not active, 1: active                                                                                                                                                                                                                                                                    |
| REG_SYSTEM_ROTOR_TYPE    | 353     | R/W |     |         | Reg               | Type of rotor control: 0 On/off, 1 Variable control                                                                                                                                                                                                                                                             |
| REG_SYSTEM_PASSIVE_HOUSE | 354     | R/W |     |         | Reg               | Passive house mode. 0: not active, 1: active (introduced PCU‑EC4 v5.09.00)                                                                                                                                                                                                                                      |

## 7.5 Registers for RH Sensor

| Name                     | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                       |
|--------------------------|---------|-----|-----|---------|-------------------|-----------------------------------------------------------|
| REG_RH_SENSOR_VALUE      | 381     | R   |     |         | Reg               | RH sensor value (%)                                       |
| REG_RH_SENSOR_DATA_VALID | 383     | R   |     |         | Reg               | Indicates that valid data from the RH sensor is available |

## 7.6 Registers for the Week Program

| Name                    | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                                   |
|-------------------------|---------|-----|-----|---------|-------------------|-------------------------------------------------------------------------------------------------------|
| REG_WP_ACTIVE           | 401     | R   |     |         | Reg + Coil (6401) | 0: Week program not active, 1: Active                                                                 |
| REG_WP_ON_LVL           | 402     | R/W | Y   |         | Reg               | Week program active speed level                                                                       |
| REG_WP_OFF_LVL          | 403     | R/W | Y   |         | Reg               | Week program inactive speed level                                                                     |
| REG_WP_WD1_PRD1_START_H | 404     | R/W | Y   |         | Reg               | Start of week program, day 1, period 1, hour. Hour                                                    |
| REG_WP_WD1_PRD1_START_M | 405     | R/W | Y   |         | Reg               | Start of week program, day 1, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD1_PRD1_END_H   | 406     | R/W | Y   |         | Reg               | End of week program, day 1, period 1, hour. Hour                                                      |
| REG_WP_WD1_PRD1_END_M   | 407     | R/W | Y   |         | Reg               | End of week program, day 1, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD1_PRD2_START_H | 408     | R/W | Y   |         | Reg               | Start of week program, day 1, period 2, hour. Hour                                                    |
| REG_WP_WD1_PRD2_START_M | 409     | R/W | Y   |         | Reg               | Start of week program, day 1, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD1_PRD2_END_H   | 410     | R/W | Y   |         | Reg               | End of week program, day 1, period 2, hour. Hour                                                      |
| REG_WP_WD1_PRD2_END_M   | 411     | R/W | Y   |         | Reg               | End of week program, day 1, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD2_PRD1_START_H | 412     | R/W | Y   |         | Reg               | Start of week program, day 2, period 1, hour. Hour                                                    |
| REG_WP_WD2_PRD1_START_M | 413     | R/W | Y   |         | Reg               | Start of week program, day 2, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD2_PRD1_END_H   | 414     | R/W | Y   |         | Reg               | End of week program, day 2, period 1, hour. Hour                                                      |
| REG_WP_WD2_PRD1_END_M   | 415     | R/W | Y   |         | Reg               | End of week program, day 2, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD2_PRD2_START_H | 416     | R/W | Y   |         | Reg               | Start of week program, day 2, period 2, hour. Hour                                                    |
| REG_WP_WD2_PRD2_START_M | 417     | R/W | Y   |         | Reg               | Start of week program, day 2, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD2_PRD2_END_H   | 418     | R/W | Y   |         | Reg               | End of week program, day 2, period 2, hour. Hour                                                      |
| REG_WP_WD2_PRD2_END_M   | 419     | R/W | Y   |         | Reg               | End of week program, day 2, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD3_PRD1_START_H | 420     | R/W | Y   |         | Reg               | Start of week program, day 3, period 1, hour. Hour                                                    |
| REG_WP_WD3_PRD1_START_M | 421     | R/W | Y   |         | Reg               | Start of week program, day 3, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD3_PRD1_END_H   | 422     | R/W | Y   |         | Reg               | End of week program, day 3, period 1, hour. Hour                                                      |
| REG_WP_WD3_PRD1_END_M   | 423     | R/W | Y   |         | Reg               | End of week program, day 3, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD3_PRD2_START_H | 424     | R/W | Y   |         | Reg               | Start of week program, day 3, period 2, hour. Hour                                                    |
| REG_WP_WD3_PRD2_START_M | 425     | R/W | Y   |         | Reg               | Start of week program, day 3, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD3_PRD2_END_H   | 426     | R/W | Y   |         | Reg               | End of week program, day 3, period 2, hour. Hour                                                      |
| REG_WP_WD3_PRD2_END_M   | 427     | R/W | Y   |         | Reg               | End of week program, day 3, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD4_PRD1_START_H | 428     | R/W | Y   |         | Reg               | Start of week program, day 4, period 1, hour. Hour                                                    |
| REG_WP_WD4_PRD1_START_M | 429     | R/W | Y   |         | Reg               | Start of week program, day 4, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD4_PRD1_END_H   | 430     | R/W | Y   |         | Reg               | End of week program, day 4, period 1, hour. Hour                                                      |
| REG_WP_WD4_PRD1_END_M   | 431     | R/W | Y   |         | Reg               | End of week program, day 4, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD4_PRD2_START_H | 432     | R/W | Y   |         | Reg               | Start of week program, day 4, period 2, hour. Hour                                                    |
| REG_WP_WD4_PRD2_START_M | 433     | R/W | Y   |         | Reg               | Start of week program, day 4, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD4_PRD2_END_H   | 434     | R/W | Y   |         | Reg               | End of week program, day 4, period 2, hour. Hour                                                      |
| REG_WP_WD4_PRD2_END_M   | 435     | R/W | Y   |         | Reg               | End of week program, day 4, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD5_PRD1_START_H | 436     | R/W | Y   |         | Reg               | Start of week program, day 5, period 1, hour. Hour                                                    |
| REG_WP_WD5_PRD1_START_M | 437     | R/W | Y   |         | Reg               | Start of week program, day 5, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD5_PRD1_END_H   | 438     | R/W | Y   |         | Reg               | End of week program, day 5, period 1, hour. Hour                                                      |
| REG_WP_WD5_PRD1_END_M   | 439     | R/W | Y   |         | Reg               | End of week program, day 5, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD5_PRD2_START_H | 440     | R/W | Y   |         | Reg               | Start of week program, day 5, period 2, hour. Hour                                                    |
| REG_WP_WD5_PRD2_START_M | 441     | R/W | Y   |         | Reg               | Start of week program, day 5, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD5_PRD2_END_H   | 442     | R/W | Y   |         | Reg               | End of week program, day 5, period 2, hour. Hour                                                      |
| REG_WP_WD5_PRD2_END_M   | 443     | R/W | Y   |         | Reg               | End of week program, day 5, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD6_PRD1_START_H | 444     | R/W | Y   |         | Reg               | Start of week program, day 6, period 1, hour. Hour                                                    |
| REG_WP_WD6_PRD1_START_M | 445     | R/W | Y   |         | Reg               | Start of week program, day 6, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD6_PRD1_END_H   | 446     | R/W | Y   |         | Reg               | End of week program, day 6, period 1, hour. Hour                                                      |
| REG_WP_WD6_PRD1_END_M   | 447     | R/W | Y   |         | Reg               | End of week program, day 6, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD6_PRD2_START_H | 448     | R/W | Y   |         | Reg               | Start of week program, day 6, period 2, hour. Hour                                                    |
| REG_WP_WD6_PRD2_START_M | 449     | R/W | Y   |         | Reg               | Start of week program, day 6, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD6_PRD2_END_H   | 450     | R/W | Y   |         | Reg               | End of week program, day 6, period 2, hour. Hour                                                      |
| REG_WP_WD6_PRD2_END_M   | 451     | R/W | Y   |         | Reg               | End of week program, day 6, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD7_PRD1_START_H | 452     | R/W | Y   |         | Reg               | Start of week program, day 7, period 1, hour. Hour                                                    |
| REG_WP_WD7_PRD1_START_M | 453     | R/W | Y   |         | Reg               | Start of week program, day 7, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD7_PRD1_END_H   | 454     | R/W | Y   |         | Reg               | End of week program, day 7, period 1, hour. Hour                                                      |
| REG_WP_WD7_PRD1_END_M   | 455     | R/W | Y   |         | Reg               | End of week program, day 7, period 1, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |
| REG_WP_WD7_PRD2_START_H | 456     | R/W | Y   |         | Reg               | Start of week program, day 7, period 2, hour. Hour                                                    |
| REG_WP_WD7_PRD2_START_M | 457     | R/W | Y   |         | Reg               | Start of week program, day 7, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50 |
| REG_WP_WD7_PRD2_END_H   | 458     | R/W | Y   |         | Reg               | End of week program, day 7, period 2, hour. Hour                                                      |
| REG_WP_WD7_PRD2_END_M   | 459     | R/W | Y   |         | Reg               | End of week program, day 7, period 2, minute. Minute. Allowed values: 0, 10, 15, 20, 30, 40, 45, 50   |

## 7.7 Registers for System Parameters

| Name                                 | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                                                                                                                          |
|--------------------------------------|---------|-----|-----|---------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG_SYSTEM_TYPE                      | 501     | R/W | Y   |         | Reg               | 0 VR400, 1 VR700, 2 VR700DK, 3 VR400DE, 4 VTC300, 5 VTC700, 12 VTR150K, 13 VTR200B, 14 VSR300, 15 VSR500, 16 VSR150, 17 VTR300, 18 VTR500, 19 VSR300DE, 20 VTC200, 21 VTC100; others ignored |
| REG_SYSTEM_PROG_V_HIGH               | 502     | R   |     |         | Reg               | PCU‑ECx main program version – high                                                                                                                                                          |
| REG_SYSTEM_PROG_V_MID                | 503     | R   |     |         | Reg               | PCU‑ECx main program version – middle                                                                                                                                                        |
| REG_SYSTEM_PROG_V_LOW                | 504     | R   |     |         | Reg               | PCU‑ECx main program version – low                                                                                                                                                           |
| REG_SYSTEM_BOOT_PROG_V_HIGH          | 505     | R   |     |         | Reg               | PCU‑ECx boot program version – high                                                                                                                                                          |
| REG_SYSTEM_BOOT_PROG_V_MID           | 506     | R   |     |         | Reg               | PCU‑ECx boot program version – middle                                                                                                                                                        |
| REG_SYSTEM_BOOT_PROG_V_LOW           | 507     | R   |     |         | Reg               | PCU‑ECx boot program version – low                                                                                                                                                           |
| REG_SYSTEM_PROG_STATE                | 508     | R   |     |         | Reg               | Program state: 1 Main program, 2 Boot loader, 3 Boot loading (request accepted)                                                                                                              |
| REG_SYSTEM_START_BOOTLOADER          | 509     | W   | N   |         | Reg               | Write non‑zero to activate boot loader. Flags: Bit0 download CD3, Bit8 download PCU‑EC3. Only via FC 6 (Write single register)                                                               |
| REG_SYSTEM_BOOTLOADER_FLAGS          | 510     | R   |     |         | Reg               | Bit0: Boot loading requested by PCU‑EC3 card                                                                                                                                                 |
| REG_SYSTEM_BRIDGE_CD3_FIRMWARE_H     | 521     | R/W |     |         | Reg               | CD2/3 program version available in Z‑wave bridge – high                                                                                                                                      |
| REG_SYSTEM_BRIDGE_CD3_FIRMWARE_M     | 522     | R/W |     |         | Reg               | CD2/3 program version available in Z‑wave bridge – middle                                                                                                                                    |
| REG_SYSTEM_BRIDGE_CD3_FIRMWARE_L     | 523     | R/W |     |         | Reg               | CD2/3 program version available in Z‑wave bridge – low                                                                                                                                       |
| REG_SYSTEM_BRIDGE_PCU_EC3_FIRMWARE_H | 521     | R/W |     |         | Reg               | PCU‑ECx program version available in Z‑wave bridge – high                                                                                                                                    |
| REG_SYSTEM_BRIDGE_PCU_EC3_FIRMWARE_M | 522     | R/W |     |         | Reg               | PCU‑ECx program version available in Z‑wave bridge – middle                                                                                                                                  |
| REG_SYSTEM_BRIDGE_PCU_EC3_FIRMWARE_L | 523     | R/W |     |         | Reg               | PCU‑ECx program version available in Z‑wave bridge – low                                                                                                                                     |
| REG_SYSTEM_CDX_PROG_V_H              | 524     | R   |     |         | Reg               | CDx program version – high (last operated CDx; 0 if none since power‑on)                                                                                                                     |
| REG_SYSTEM_CDX_PROG_V_M              | 525     | R   |     |         | Reg               | CDx program version – middle (last operated CDx; 0 if none)                                                                                                                                  |
| REG_SYSTEM_CDX_PROG_V_L              | 526     | R   |     |         | Reg               | CDx program version – low (last operated CDx; 0 if none)                                                                                                                                     |
| REG_STORE_NVM                        | 549     | W   | N   |         | Reg               | Write 165 to store: REG_FAN_SPEED_LEVEL, REG_HC_TEMP_LVL, REG_FAN_SF/EF_FLOW_LOW/NOM/HIGH. Only via FC 6.                                                                                    |

## 7.8 Registers for Clock

| Name         | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                 |
|--------------|---------|-----|-----|---------|-------------------|-------------------------------------|
| REG_CLK_S    | 551     | R/W | Y   |         | Reg               | Clock seconds (0–59)                |
| REG_CLK_M    | 552     | R/W | Y   |         | Reg               | Clock minutes (0–59)                |
| REG_CLK_H    | 553     | R/W | Y   |         | Reg               | Clock hours (0–23)                  |
| REG_CLK_D    | 554     | R/W | Y   |         | Reg               | Clock day of month (1–31)           |
| REG_CLK_MNTH | 555     | R/W | Y   |         | Reg               | Clock month (1–12)                  |
| REG_CLK_Y    | 556     | R/W | Y   |         | Reg               | Clock year (0 = 2000)               |
| REG_CLK_WD   | 557     | R   |     |         | Reg               | Clock day of week (0..6 = Mon..Sun) |

## 7.9 Registers for the Filter

| Name            | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                        |
|-----------------|---------|-----|-----|---------|-------------------|--------------------------------------------|
| REG_FILTER_PER  | 601     | R/W | Y   |         | Reg               | Filter replacement time in months          |
| REG_FILTER_DAYS | 602     | R/W | Y   |         | Reg               | Elapsed days since last filter replacement |

## 7.10 Registers for VTC Defrosting

| Name                   | Address | R/W | NVM | Scaling | Access (Reg/Coil)  | Description/Remarks                                                                                |
|------------------------|---------|-----|-----|---------|--------------------|----------------------------------------------------------------------------------------------------|
| REG_DEFR_STATE_VTC     | 651     | R   |     |         | Reg                | Defrosting state: 0 No defrost, 2 Bypass defrosting, 3 Stop defrosting, 4 Defrost error            |
| REG_DEFR_CONFIGURATION | 652     | R   |     |         | Reg                | Defrosting configuration: 0 A, 1 B, 2 C (not supported by PCU‑EC4), 3 D (not supported by PCU‑EC4) |
| REG_DEFR_UNBAL_ALLOWED | 653     | R/W | Y   |         | Reg + Coil (10433) | Unbalance allowed. 0 Not allowed, 1 Allowed                                                        |
| REG_DEFR_MODE_VTC      | 654     | R/W | Y   |         | Reg                | Defrosting mode. Allowed values: if no RH sensor: 1–5; with RH: 1–3 (Soft, Normal, Hard)           |
| REG_RH_SENSOR_PRESENT  | 655     | R/W |     |         | Reg                | RH sensor presence: 0 Not used, 1 Connected and used                                               |

## 7.11 Register for VR/VTR Defrosting

| Name              | Address | R/W  | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                |
|-------------------|---------|------|-----|---------|-------------------|----------------------------------------------------|
| REG_DEFR_STATE_VR | 671     | R    |     |         | Reg               | State: 0 Inactive, 1 Low temperature, 2 Defrosting |
| REG_DEFR_MODE_VR  | 672     | R/RW | Y   |         | Reg               | Defrosting mode. Allowed values 0–5                |

## 7.12 Registers for the Digital Inputs

| Name                              | Address | R/W | NVM | Scaling | Access (Reg/Coil)         | Description/Remarks                                                                                                                                                                                            |
|-----------------------------------|---------|-----|-----|---------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG_DI_ALL                        | 701     | R/W |     |         | Reg + Coils (11201–11207) | Write: activate functions. Read: physical input states. Bit0 DI1, Bit1 DI2, Bit2 DI3, Bit3 Heater on/off, Bit4 Extended running/Boost, Bit5 Rotor/Damper (read‑only), Bit6 Home/Leave, Bit7 not used (write 0) |
| REG_DI_EXT_RUNNING_M              | 702     | R/W | Y   |         | Reg                       | Extended running time in minutes                                                                                                                                                                               |
| REG_DI_EXT_RUNNING_SPEED_LVL      | 703     | R/W | Y   |         | Reg                       | Fan speed during extended running: 0 Off, 1 Low, 2 Normal, 3 High                                                                                                                                              |
| REG_DI1_SF_LVL                    | 704     | R/W | Y   |         | Reg                       | Supply fan speed level when DI1 active                                                                                                                                                                         |
| REG_DI1_EF_LVL                    | 705     | R/W | Y   |         | Reg                       | Extract fan speed level when DI1 active                                                                                                                                                                        |
| REG_DI2_SF_LVL                    | 706     | R/W | Y   |         | Reg                       | Supply fan speed level when DI2 active                                                                                                                                                                         |
| REG_DI2_EF_LVL                    | 707     | R/W | Y   |         | Reg                       | Extract fan speed level when DI2 active                                                                                                                                                                        |
| REG_DI3_SF_LVL                    | 708     | R/W | Y   |         | Reg                       | Supply fan speed level when DI3 active                                                                                                                                                                         |
| REG_DI3_EF_LVL                    | 709     | R/W | Y   |         | Reg                       | Extract fan speed level when DI3 active                                                                                                                                                                        |
| REG_DI_FUNCTIONS                  | 710     | R   |     |         | Reg                       | Functions active due to DIs. Bits as for DI_ALL (bit5 Rotor/Damper)                                                                                                                                            |
| REG_DI_MODBUS                     | 711     | R   |     |         | Reg                       | Latest value written to REG_DI_ALL. Bits: 0 DI1, 1 DI2, 2 DI3, 3 Heater, 4 Extended running, 5 n/a, 6 Home/Leave, 7 n/a                                                                                        |
| REG_DI_WIRELESS                   | 712     | R   |     |         | Reg                       | OR of all wireless inputs. Bits as in REG_DI_MODBUS                                                                                                                                                            |
| REG_DI_REMAINING_TIME_1           | 713     | R   |     |         | Reg                       | Remaining time (s) for DI1 delay                                                                                                                                                                               |
| REG_DI_REMAINING_TIME_2           | 714     | R   |     |         | Reg                       | Remaining time (s) for DI2 delay                                                                                                                                                                               |
| REG_DI_REMAINING_TIME_3           | 715     | R   |     |         | Reg                       | Remaining time (s) for DI3 delay                                                                                                                                                                               |
| REG_DI_REMAINING_TIME_EXT_RUNNING | 716     | R   |     |         | Reg                       | Remaining time (s) for Extended running delay                                                                                                                                                                  |

## 7.13 Registers for PCU-PB

| Name              | Address | R/W | NVM | Scaling | Access (Reg/Coil)         | Description/Remarks                                                                      |
|-------------------|---------|-----|-----|---------|---------------------------|------------------------------------------------------------------------------------------|
| REG_PCU_PB_RELAYS | 751     | R   |     |         | Reg + Coils (12001–12003) | Coils: 12001 preheater on, 12002 reheater on, 12003 common relay for heater/preheater on |

## 7.14 Registers for Alarms

| Name                    | Address | R/W | NVM | Scaling | Access (Reg/Coil)         | Description/Remarks                                                                                                                                                                                                                                              |
|-------------------------|---------|-----|-----|---------|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG_ALARMS_ALL          | 801     | R   |     |         | Reg + Coils (12801–12812) | Coils: 12801 Filter, 12802 Fan, 12803 -, 12804 Rotor, 12805 Frost, 12806 PCU‑PB, 12807 Temp sensor, 12808 Emergency thermostat, 12809 Damper, 12810 Low SS, 12811 Defrost, 12812 RH sensor. 0: not active, 1: active                                             |
| REG_ALARMS_RELAY_ACTIVE | 802     | R   |     |         | Reg + Coil (12817)        | Alarm relay active. 0 Not active, 1 Active                                                                                                                                                                                                                       |
| REG_ALARMS_ALL_DETAILED | 803     | R   |     |         | Reg                       | All alarm flags incl. temp sensor status. Bits: 0 Filter,1 Fan,2 Rotor,3 Frost,4 PCU‑PB,5 Emergency thermostat,6 Damper,7 Low SS,8 Defrost,9 RH sensor,10 SA sensor,11 EA sensor,12 Exhaust/Preheater sensor,13 Overtemp/Frost prot sensor,14 Outdoor air sensor |

## 7.15 Register for Demand Control

| Name                          | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                             |
|-------------------------------|---------|-----|-----|---------|-------------------|-------------------------------------------------------------------------------------------------|
| REG_DEMC_CO2_SP               | 851     | R/W |     |         | Reg               | CO₂ setpoint. Range 0–2000; 0=Off                                                               |
| REG_DEMC_CO2_P_BAND           | 852     | R/W |     |         | Reg               | CO₂ P-Band. Range 1–2000                                                                        |
| REG_DEMC_CO2_I_TIME           | 853     | R/W |     |         | Reg               | CO₂ I-Time. Range 1–120; 0: no integration                                                      |
| REG_DEMC_RH_SP_SUMMER         | 854     | R/W |     |         | Reg               | RH SP (Summer). Range 0–100; 0=Off. (Old name REG_DEMC_RH_SP before PCU‑EC4 v5.09.00)           |
| REG_DEMC_RH_P_BAND            | 855     | R/W |     |         | Reg               | RH P-Band. Range 1–100                                                                          |
| REG_DEMC_RH_I_TIME            | 856     | R/W |     |         | Reg               | RH I-Time. Range 1–120; 0: no integration                                                       |
| REG_DEMC_STATE                | 857     | R   |     |         | Reg               | 0 Start up, 1 Waiting for sensor network, 2 Waiting for sensor data, 3 Auto mode, 4 Normal mode |
| REG_DEMC_MODBUS_CO2_VALUE     | 858     | W   |     |         | Reg               | CO₂ value in ppm. Range 0–2000                                                                  |
| REG_DEMC_MODBUS_RH_VALUE      | 859     | W   |     |         | Reg               | RH value in %. Range 0–100                                                                      |
| REG_DEMC_MODBUS_CO2_OUT       | 860     | R   |     |         | Reg               | Output of PI controller for CO₂ regulation                                                      |
| REG_DEMC_MODBUS_RH_OUT        | 861     | R   |     |         | Reg               | Output of PI controller for RH regulation                                                       |
| REG_DEMC_ALLOWED              | 862     | R   |     |         | Reg               | Bit0: 0 Auto mode cannot be activated, 1 Auto mode can be activated. Bits1–15: not used         |
| REG_DEMC_RH_SP_WINTER         | 863     | R/W |     |         | Reg               | RH SP (Winter). Range 0–100 (introduced PCU‑EC4 v5.09.00)                                       |
| REG_DEMC_SUMMER_WINTER_MODE   | 864     | R   |     |         | Reg               | 0 Summer, 1 Winter (introduced PCU‑EC4 v5.09.00)                                                |
| REG_DEMC_SUMMER_WINTER_CNTR_H | 865     | R   |     |         | Reg               | Highest 16 bits of remaining time until summer mode                                             |
| REG_DEMC_SUMMER_WINTER_CNTR_L | 866     | R   |     |         | Reg               | Lowest 16 bits of remaining time until summer mode                                              |

## 7.16 Register for Wireless Network

| Name                    | Address  | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks                                                                                         |
|-------------------------|----------|-----|-----|---------|-------------------|-------------------------------------------------------------------------------------------------------------|
| REG_WL_NODE_1_TYPE      | 901      | R   |     |         | Reg               | 0 No connected, 1 CO₂ sensor, 2 RH sensor, 3 DI module, 4 User interface                                    |
| REG_WL_NODE_1_VALUE_T   | 902      | R   |     |         | Reg + Coils       | Value depends on node type. For DI module read coils: 14417 input1, 14418 input2. Otherwise CO₂ or RH value |
| REG_WL_NODE_1_STATUS    | 903      | R   |     |         | Reg               | 0 not bound, 1 OK, 2 Battery failure, 3 Communication failure, 4 No network, 5 Sensor failure               |
| REG_WL_NODE_2_xx        | 911–920  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_3_xx        | 921–930  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_4_xx        | 931–940  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_5_xx        | 941–950  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_6_xx        | 951–960  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_7_xx        | 961–970  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_8_xx        | 971–980  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_9_xx        | 981–990  | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_NODE_10_xx       | 991–1000 | -   |     |         |                   | As for 901–910                                                                                              |
| REG_WL_DI_CONNECTION_1  | 1001     | R   |     |         |                   | 0 Not connected, 1 DI1, 2 DI2, 3 DI3, 4 DI4, 5 DI5, 6 not accepted, 7 DI7; others: not accepted             |
| REG_WL_DI_CONNECTION_2  | 1002     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_3  | 1003     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_4  | 1004     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_5  | 1005     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_6  | 1006     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_7  | 1007     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_8  | 1008     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_9  | 1009     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_10 | 1010     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_11 | 1011     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_12 | 1012     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_13 | 1013     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_14 | 1014     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_15 | 1015     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_16 | 1016     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_17 | 1017     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_18 | 1018     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_19 | 1019     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |
| REG_WL_DI_CONNECTION_20 | 1020     | R   |     |         |                   | As for REG_WL_DI_CONNECTION_1                                                                               |

## 7.17 Registers for RH Transfer Control

| Name            | Address | R/W | NVM | Scaling | Access (Reg/Coil) | Description/Remarks              |
|-----------------|---------|-----|-----|---------|-------------------|----------------------------------|
| REG_RH_TC_SP    | 1101    | R/W |     |         | Reg               | Setpoint for RH transfer control |
| REG_RH_TC_PBAND | 1102    | R/W |     |         | Reg               | P-band for RH transfer control   |
| REG_RH_TC_ITIME | 1103    | R/W |     |         | Reg               | I-time for RH transfer control   |
| REG_RH_TC_OUT   | 1104    | R   |     |         | Reg               | Output of RH transfer controller |

