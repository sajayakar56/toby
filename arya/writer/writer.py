from collections import deque
from .Pad import Pad


class Writer():
    def __init__(self):
        super().__init__()
        self.p = Pad()
        self.frames = deque()

    # Function to perform multiple frames
    def parse(self, s: str) -> None:
        # Frames are split by semicolons
        frames = s.split(";")
        self.frames.extend(frames)

    # Sends one frame's worth of inputs
    def advance(self) -> None:
        if not len(self.frames):
            return
        frame = self.frames.popleft()
        actions = frame.split(",")
        for action in actions:
            self._do_action(action)

    # will re-instantiate the linked list
    def clear(self) -> None:
        return None
        
    # Helper that actually performs one action
    def _do_action(self, s: str) -> None:
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
