from .StateManager import MemoryMap
from .StateManager import StateManager as sm
from .PadManager import PadManager
import time


# Things to do:
# - Should definitely have the loop on a run function
#   : Would have the "waiting" at the highest level, so that the AI can perform other tasks meanwhile
# - Also, have routine to be overwritten which is something that is run every update
class AI:
    def __init__(self):
        self.pm = PadManager()
        self.sm = sm
        self.actions = []

    def do(self, action: list) -> None:
        if not self.actions:
            self.actions += action
        
    # Wrapper for pad
    def parse(self, s: str) -> None:
        try:
            self.pm.parse(s)
        except Exception:
            print("Malformed Query:", s)

    def run(self) -> None:
        sTime = time.time()
        while True:
            self.routine()
            if (time.time() - sTime > 1/60) and self.actions:
                frame = self.actions.pop(0)
                for command in frame:
                    self.parse(command)
                sTime = time.time()
            
    def routine(self) -> None:
        return None

    @property
    def performing(self) -> bool:
        return len(self.actions) != 0
                

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
                ("p R",),
                ("r",)]

    @property
    def dTilt(self) -> list:
        return [("t MAIN 0.5 0.6", "p A"),
                ("r",)]

    @property
    def walkLeft(self) -> list:
        return [("t MAIN 0.5 0.5",),
                ("t MAIN 0.45 0.5",),
                ("t MAIN 0.4 0.5",)]

    @property
    def walkRight(self) -> list:
        return [("t MAIN 0.5 0.5",),
                ("t MAIN 0.55 0.5",),
                ("t MAIN 0.6 0.5",)]

    
def _wait_frame():
    startTime = time.time()
    while (time.time() - startTime < 1/60):
        pass
