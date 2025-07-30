from typing import List
from fastcrc import crc16

proto_header = bytes.fromhex("02020016001200403083ff1b02")
cmd_header   = bytes.fromhex("5560010ff00300")
terminator = bytes.fromhex("c4")

def getCrc(payload: bytes) -> bytes:
    data = cmd_header + payload
    return crc16.modbus(data).to_bytes(2, 'little')

# Payload structure:
# protocol header + command header + sequence id (counter) + command payload + 00 (common in every command) + crc + c4 (terminator)

def finalPayload(payload: str, counter: int) -> bytes:
    payload = counter.to_bytes() + bytes.fromhex(payload + "00")
    final = proto_header + cmd_header + payload + getCrc(payload) + terminator

    print(final.hex(), counter)
    return final