import os
import math
from action import *
from MemoryManager import MemoryManager
from pad import Pad, Button, Stick
import time
from os.path import expanduser
home = expanduser("~")
dolphin = home + "/Library/Application Support/Dolphin/"

class AI:
    def __init__(self):
        self.mm = MemoryManager(dolphin)
        self.pad = Pad(dolphin)
        self.performing = False
        self.actions = []

    def perform(self):
        if self.performing:
            return
        self.performing = True
        if self.actions:
            action = self.actions.pop(0)
            for frame in action.frames:
                startTime = time.time()
                for sa in frame.subs:
                    self.parse_pad(sa)
                while (time.time() - startTime < 1/60):
                    pass
        self.pad.reset()
        self.performing = False

    def queue_action(self, action):
        self.actions += action
        
    # Public
    def do(self, action):
        if not self.performing:
            self.chill()
            self.queue_action(action)
            self.perform()
        
    def chill(self):
        self.actions = []

    def distance_x(self):
        p1x, p2x = self.mm.get("P1 X", "P2 X")
        if (p1x and p2x):
            distance = abs(p1x - p2x)
            return distance
        if not p2x:
            self.do([self.nudgeLeft])
            return self.distance_x()
        return None

    def parse_pad(self, sub_action):
        if sub_action.type == "press":
            self.pad.press_button(Button[sub_action.input])
        elif sub_action.type == "release":
            self.pad.release_button(Button[sub_action.input])
        elif sub_action.type == "tilt":
            self.pad.tilt_stick(Stick[sub_action.input], sub_action.x, sub_action.y)

    wavedash = Action("Wavedash", (Frame(SA("press", "X"), SA("tilt", "MAIN", 0.5, 1)),
                                   Frame(),
                                   Frame(SA("release", "X")),
                                   Frame(),
                                   Frame(SA("press", "R")),))
    nudgeLeft = Action("Nudge Left", (Frame(SA("tilt", "MAIN", 0.4, 0.5)),
                                      Frame()))
    dTilt = Action("Down Tilt", (Frame(SA("tilt", "MAIN", 0.5, 0.65), SA("press", "A"))))

