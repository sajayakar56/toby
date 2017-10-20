import struct
import time
from io import StringIO
import threading
import math
from .mmap import MemoryMap, Player, State

class Reader():
    def __init__(self):
        super().__init__()
        self.mm = MemoryMap()
        self.p1 = Player(1, self.mm)
        self.p2 = Player(2, self.mm)
        self.state = State(self.mm)

    def update(self):
        self.mm.update()            
