import os
import math
from aria.action import *
from aria.MemoryManager import MemoryManager
from aria.pad import Pad, Button, Stick
import time
from os.path import expanduser
home = expanduser("~")
dolphin = home + "/Library/Application Support/Dolphin/"

class AI:
    def __init__(self):
        self.mm = MemoryManager(dolphin)
        self.pad = Pad(dolphin)
        self.performing = False

    def perform(self, actions):
        if self.performing:
            return
        self.performing = True
        while actions:
            action = actions.pop()
            for frame in action.frames:
                startTime = time.time()
                for sa in frame.subs:
                    self.parse_pad(sa)
                while (time.time() - startTime < 1/60):
                    pass
        self.pad.reset()
        self.performing = False

    def x_dist(self):
        self.mm.update()
        p1x, p2x = self.mm.get("P1 X", "P2 X")
        if (p1x and p2x):
            distance = abs(p1x - p2x)
            return distance
        if not p2x:
            self.perform([nudgeLeft])
            return self.x_dist()
        return None

    def parse_pad(self, sub_action):
        if sub_action.type == "press":
            self.pad.press_button(Button[sub_action.thing])
        elif sub_action.type == "release":
            self.pad.release_button(Button[sub_action.thing])
        elif sub_action.type == "tilt":
            self.pad.tilt_stick(Stick[sub_action.thing], sub_action.x, sub_action.y)
