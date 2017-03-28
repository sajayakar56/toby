class Action:
    def __init__(self, name, frames):
        self.name = name
        self.frames = frames

    def __next__(self):
        return self.subs.pop()

    def __repr__(self):
        return self.name


class SA:
    def __init__(self, type, inp, x = 0, y = 0):
        self.type = type
        self.input = inp
        if self.type == "tilt":
            self.x = x
            self.y = y

class Frame:
    def __init__(self, *sas):
        self.subs = sas

