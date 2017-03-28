import socket
import os

# Heavily adapted from spxtr/p3
class MemoryWatcher:
    def __init__(self, path):
        self.path = path
        try:
            os.unlink(self.path)
        except OSError:
            pass

    def __enter__(self):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        self.sock.settimeout(0.001)
        self.sock.bind(self.path)
        return self

    def __exit__(self, *args):
        self.sock.close()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            data = self.sock.recvfrom(1024)[0].decode('utf-8').splitlines()
        except socket.timeout:
            return None
        return data
