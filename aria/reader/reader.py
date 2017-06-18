import struct
import time
from io import StringIO
import threading
import math
from .mmap import MemoryMap, Player

class Reader(threading.Thread):
    def __init__(self):
        super().__init__()
        self.mm = MemoryMap()
        self.p1 = Player(1, self.mm)
        self.p2 = Player(2, self.mm)
        self.start()

    def run(self):
        while True:
            self.mm.update()

_reader = Reader()
# Namespace
p1 = _reader.p1
p2 = _reader.p2

            
