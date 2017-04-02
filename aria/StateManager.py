from .MemoryWatcher import MemoryWatcher
import struct
from io import StringIO


class MemoryMap:
    # map between int32 addr -> value: bytes
    data = {}

    def __init__(self):
        self.mw = MemoryWatcher()

    def lookup(self, addr: int) -> bytes:
        self._update()
        if addr in self.data:
            return self.data[addr]
        return None

    # Only receives one addresses value at a time
    # For now, hardcoding in number of refreshes.  Revisit
    def _update(self, t: int = 20) -> None:
        received_data = self.mw.receive()
        while received_data:
            addr, value = received_data
            self.data[addr] = value
            received_data = self.mw.receive()



class Player:
    def __init__(self, number, mm):
        self.number = number
        self.mult = number - 1
        self.mm = mm
            
    @property
    def x(self) -> float:
        base_addr = 4534416
        offset = 3728
        addr = base_addr + (self.mult * offset)
        raw_value = self.mm.lookup(addr)
        return_val = bytes_to_float(raw_value)
        return none(return_val, 0)

    @property
    def y(self) -> float:
        base_addr = 4534420
        offset = 3728
        addr = base_addr + (self.mult * offset)
        raw_value = self.mm.lookup(addr)
        return_val = bytes_to_float(raw_value)
        return none(return_val, 0)

    @property
    def dmg(self) -> int:
        base_addr = 4534496
        offset = 3728
        addr = base_addr + (self.mult * offset)
        raw_value = self.mm.lookup(addr)
        return_val = bytes_to_int(raw_value)
        return none(return_val, 0)

    @property
    def stocks(self) -> int:
        base_addr = 4534542
        offset = 3728
        addr = base_addr + (self.mult * offset)
        raw_value = self.mm.lookup(addr)
        return_val = bytes_to_int(raw_value)
        return none(return_val, 0)

    def __str__(self):
        string = StringIO()
        string.write("Player %d\n" % self.number)
        string.write("x : %s\n" % self.x)
        string.write("y : %s\n" % self.y)
        string.write("%% : %s\n" % self.dmg)
        return string.getvalue()


def bytes_to_float(b: bytes) -> float:
    if not b:
        return None
    return struct.unpack(">f", b)[0]


def bytes_to_int(b: bytes) -> float:
    if not b:
        return None
    b = b.ljust(4, b'\x00')    
    return struct.unpack("<i", b)[0]

def none(val, other):
    if not val:
        return other
    return val

class StateManager:
    _mm = MemoryMap()
    p1 = Player(1, _mm)
    p2 = Player(2, _mm)
