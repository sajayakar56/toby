from .MemoryWatcher import MemoryWatcher
import struct


class MemoryMap:
    # map between addr: str -> value: bytes
    data = {}

    def __init__(self):
        self.mw = MemoryWatcher()

    def lookup(self, name: str, T: type = float) -> type:
        self._update()
        addr = alias[name]
        if addr in self.data:
            return self._convert(self.data[addr], T)
        return None

    def _convert(self, val: bytes, T: type) -> type:
        if (T == float):
            return struct.unpack(">f", val)[0]
        if (T == int):
            val = val.ljust(4, b'\x00')
            return struct.unpack("<i", val)[0]
    
    def _update(self) -> None:
        received_data = self.mw.receive()
        if received_data:
            addr, value = received_data
            self.data[addr] = value

            
alias = {"P1 X": "00453090",
         "P1 Y": "00453094",
         "P1 %": "004530E0",
         "P2 X": "00453F20",
         "P2 Y": "00453F24",
         "P2 %": "00453F70"}
