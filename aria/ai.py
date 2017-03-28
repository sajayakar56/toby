from .MemoryMap import MemoryMap
from .PadManager import PadManager
import time


class AI:
    def __init__(self):
        self.mm = MemoryMap()
        self.pm = PadManager()

    def do(self, action: list) -> None:
        for frame in action:
            for command in frame:
                self.parse(command)
            _wait_frame()
        self.parse("r")
        
    # Wrapper for mm.lookup, not sure if should be public
    def lookup(self, name: str, T: type = float) -> type:
        return self.mm.lookup(name, T)

    # Yet another wrapper, not sure
    def parse(self, s: str) -> None:
        try:
            self.pm.parse(s)
        except Exception:
            print("Malformed Query:", s)

    # Actions
    # Wavedashes from range [0, 1], where 0.5 is wavedash in place
    @staticmethod
    def waveDash(x: int) -> list:
        y = 0.65
        s = "t MAIN " + str(x) + " " + str(y)
        return [(s, "p X"),
                (),
                (),
                (),
                (),
                ("p R",)]

    @staticmethod
    def dTilt() -> list:
        return [("t MAIN 0.5 0.6", "p A")]

    
def _wait_frame():
    startTime = time.time()
    while (time.time() - startTime < 1/60):
        pass
