import socket
import os
import struct
home = os.path.expanduser("~")


# Source: spxtr/p3
class MemoryWatcher:
    def __init__(self):
        self.path = home + "/Library/Application Support/Dolphin/MemoryWatcher/MemoryWatcher"
        try:
            os.unlink(self.path)
        except OSError:
            pass
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.settimeout(0.001)
        self.sock.bind(self.path)

    def receive(self) -> [str, bytes]:
        try:
            # recvfrom returns (bytes, '')
            # splits the data into [addr, val]
            data = self.sock.recvfrom(1024)[0].split(b'\n')
            # removes the \x00 from the end of addr
            data[1] = data[1][:-1]
            # turns the addr into an int
            data[0] = int(data[0], 16)
            # Handling for resetting value?
            if data[1] != b'0':
                # turns the value into true bytes
                data[1] = hex_string_to_bytes(data[1])
            else:
                data[1] = bytes(0)
        except socket.timeout:
            return None
        return data


def hex_string_to_bytes(hex_string: bytes) -> bytes:
    if len(hex_string) % 2 != 0:
        hex_string = b'0' + hex_string
    return bytes.fromhex(hex_string.decode("utf-8"))
    

if __name__ == "__main__":
    mw = MemoryWatcher()
    while True:
        data = mw.receive()
        if data:
            print(data)
            break
