from .StateManager import MemoryMap
from .StateManager import StateManager as sm
from .PadManager import PadManager
import time
import threading

# Things to do:
# - Should definitely have the loop on a run function
#   : Would have the "waiting" at the highest level, so that the AI can perform other tasks meanwhile
# - Also, have routine to be overwritten which is something that is run every update
class AI(threading.Thread):
    def __init__(self):
        super().__init__()
        self.pm = PadManager()
        self.sm = sm()
        self.actions = []
        self.tick = 1/60
        self.start()
        
    def do(self, action: str) -> None:
        action = action.split("; ")
        self.actions = action
        
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
            if (time.time() - sTime > self.tick) and self.actions:
                self._perform()
                sTime = time.time()

    def stop(self) -> None:
        self.actions = []

    def _perform(self) -> None:
        frame = self.actions.pop(0)
        frame = frame.split(", ")
        for command in frame:
            self.parse(command)
            
    def routine(self) -> None:
        return None

    @property
    def performing(self) -> bool:
        return len(self.actions) != 0

    # Actions
    # Wavedashes from range [0, 1], where 0.5 is wavedash in place
    @staticmethod
    def waveDash(x: float = 0.5) -> str:
        x = float(x)
        y = 0.65
        s = "t MAIN " + str(x) + " " + str(y)
        return "%s, p X; -; -; -; -; p R; r" % s

    @property
    def dTilt(self) -> str:
        return "t MAIN 0.5 0.6, p A; r"

    @property
    def uTilt(self) -> str:
        return "t MAIN 0.5 0.4, p A; r"

    @property
    def walkLeft(self) -> str:
        return "t MAIN 0.5 0.5; t MAIN 0.45 0.5; t MAIN 0.4 0.5"

    @property
    def walkRight(self) -> str:
        return "t MAIN 0.5 0.5; t MAIN 0.55 0.5; t MAIN 0.6 0.5"

    @property
    def crouch(self) -> str:
        return "t MAIN 0.5 0.6; t MAIN 0.5 1"

    @property
    def jab(self) -> str:
        return "p A"

    def _wait_frame(self):
        startTime = time.time()
        while (time.time() - startTime < 1/60):
            pass
