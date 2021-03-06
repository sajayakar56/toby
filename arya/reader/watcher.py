import socket
import os
import struct
import binascii
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
        # self.sock.settimeout(0.001)
        self.sock.bind(self.path)

    def receive(self) -> [int, bytes]:
        try:
            data = self.sock.recvfrom(32)[0].decode('utf-8').splitlines()
        except socket.timeout:
            return None
        if " " in data[0]:
            addr, offset = data[0].split()
            data[0] = int(addr, 16) + int(offset, 16)
        else:
            data[0] = int(data[0], 16)
        data[1] = binascii.unhexlify(data[1].strip('\x00').zfill(8))
        return data
        # try:
        #     # splits the data into [addr, val]
        #     data = self.sock.recvfrom(32)[0].split(b'\n')
        #     # removes the \x00 from the end of addr
        #     data[1] = data[1][:-1]
        #     # adds the memory addr to its offset
        #     if 32 in data[0]:
        #         addr, offset = data[0].split(b' ')
        #         data[0] = int(addr, 16) + int(offset, 16)
        #     else:
        #         # turns the addr into an int
        #         data[0] = int(data[0], 16)
        #     # Handling for resetting value?
        #     if data[1] != b'0':
        #         # turns the value into true bytes
        #         data[1] = hex_string_to_bytes(data[1])
        #     else:
        #         data[1] = bytes(0)
        # except socket.timeout:
        #     return None
        # return data


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
