from aria import *
from aria.action import wavedash
import os
import math
from os.path import expanduser
home = expanduser("~")

dolphin = home + "/Library/Application Support/Dolphin/"
mm = MemoryManager(dolphin)
p = Pad(dolphin)

def print_clear(*s):
    os.system("clear")
    print(s)

# Testing Memory Manager
def mem_test():
    x = MemoryManager()
    prev = None
    while True:
        data = str(x)
        if data and prev != data:
            prev = data
            print_clear(data)

# Printing out the distance from chars!            
def distance_test():
    mm = MemoryManager()
    prev = None
    while True:
        p1x, p1y, p2x, p2y = mm.get("P1 X",
                                    "P1 Y",
                                    "P2 X",
                                    "P2 Y")
        s = (p1x, p1y, p2x, p2y)
        if s != prev:
            if None not in s:
                
                distance = math.sqrt((p2x - p1x)**2 +
                                 (p2y - p1y)**2)
                print_clear("Distance:", distance)
                prev = s

# Jump input test (spams jump)
def jump():
    while True:
        p.press_button(Button.X)
        p.release_button(Button.X)

# Distance and input test
# When within 15u, crouches
def crouch_when_near():
    p.tilt_stick(Stick.MAIN, .4, .4)
    p.reset()
    mm.update()
    while True:
        p1x, p2x = mm.get("P1 X", "P2 X")
        if (p1x and p2x):
            distance = abs(p1x - p2x)
            if (distance < 15):
                p.tilt_stick(Stick.MAIN, .5, 1)
            else:
                p.reset()

# AI tests begin
def wavedash_if_near():
    ai = AI()
    while True:
        distance = ai.x_dist()
        if distance:
            if distance < 20:
                ai.perform([wavedash])

wavedash_if_near()
