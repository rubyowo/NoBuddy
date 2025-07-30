from enum import StrEnum

# Command Format:
# 0x01 (Set ANC Mode) 0x1..0x7 (Mode)
class ANCPayloads(StrEnum):
  HIGH          = "01 01"
  MID           = "01 02"
  LOW           = "01 03"
  ADAPTIVE      = "01 04"

  TRANSPARENCY  = "01 07"
  OFF           = "01 05"