from enum import StrEnum

# Command Format:
# 0x01 (Set Mode) 0x4,0x7,0x5 (Mode)
class ANCPayloads(StrEnum):
  ENABLED      = "01 04"
  TRANSPARENCY = "01 07"
  DISABLED     = "01 05"