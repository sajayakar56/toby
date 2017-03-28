import socket
import os
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
            # removes the \x00 from the end of val
            data[1] = data[1][:-1]
            # turns the address to a string
            data[0] = data[0].decode("utf-8")
            # turns the value into true bytes
            data[1] = hex_string_to_bytes(data[1])
        except socket.timeout:
            return None
        return data


def hex_string_to_bytes(hex_string: bytes):
    return bytes.fromhex(hex_string.decode("utf-8"))


if __name__ == "__main__":
    mw = MemoryWatcher()
    while True:
        data = mw.receive()
        if data:
            print(data)
            break
