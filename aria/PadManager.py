from .Pad import *


class PadManager:
    def __init__(self):
        self.p = Pad()

    # Parses button command and calls appropriate Pad method
    def parse(self, s: str) -> None:
        # press A -> "p A"
        # tilt main 0.5, 0.5 -> "t MAIN 0.5 0.5"
        # trigger 0.5 -> "tr R 0.5"
        # reset -> "r"
        # release A -> "r A"
        s = s.split(" ")
        if s[0] == "r":
            if len(s) == 1:
                self.p.reset()
            else:
                button = s[1]
                assert button in dir(Button)
                self.p.release_button(Button[button])
        elif s[0] == "p":
            button = s[1]
            assert button in dir(Button)
            self.p.press_button(Button[button])
        elif s[0] == "t":
            x = float(s[2])
            y = float(s[3])
            self.p.tilt_stick(Stick[s[1]], x, y)
        elif s[0] == "tr":
            amt = float(s[2])
            self.p.press_trigger(Trigger[s[1]], amt)
