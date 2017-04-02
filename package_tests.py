import aria
from aria.StateManager import State as s
import os


def memory_map_tests():
    prev = 0.0
    while True:
        data = s.p1.x
        if prev != data:
            print(data)
            prev = data



def ai_parser():
    x = aria.AI()
    while True:
        x.parse(input())


def ai_dTilt():
    x = aria.AI()
    x.do(x.dTilt)


def ai_waveDash():
    x = aria.AI()
    x.do(x.waveDash(0))


def mm_print():
    x = aria.AI()
    prev = ""
    while True:
        string = str(x.mm)
        if (string != prev):
            print(string)
            prev = string




if __name__ == "__main__":
    memory_map_tests()