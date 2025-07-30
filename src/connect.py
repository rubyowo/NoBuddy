import typing
import bluetooth
from payloads import *
from utils import finalPayload

class RFCOMMSocket(bluetooth.BluetoothSocket):
    def __init__(self, proto=bluetooth.RFCOMM, _sock=None):
        super().__init__(proto, _sock)
        self.counter = 0

    @staticmethod
    def find_rfcomm_port(device_mac, uuid = "AEAC4A03-DFF5-498F-843A-34487CF133EB") -> int:
        """
        Find the RFCOMM port number for a given bluetooth device
        """
        services: List[Dict] = bluetooth.find_service(address=device_mac, uuid=uuid)

        for service in services:
            if "protocol" in service.keys() and service["protocol"] == "RFCOMM":
                return int(service["port"])
        # Raise Interface error when the required service is not offered my the end device
        raise bluetooth.BluetoothError("Couldn't find the RFCOMM port number. Perhaps the device is offline?")

    def send(self, payload: str):
        return super().send(finalPayload(payload, self.counter))
        self.counter += 1


mac = "3C:B0:ED:30:92:B3"

sock = RFCOMMSocket()
port = sock.find_rfcomm_port(mac)
sock.connect((mac, port))

sock.send(ANCPayloads.ENABLED)
sock.send(ANCPayloads.TRANSPARENCY)
sock.send(ANCPayloads.DISABLED)

sock.close()

