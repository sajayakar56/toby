class Action:
    def __init__(self, name, frames):
        self.name = name
        self.frames = frames

    def __next__(self):
        return self.subs.pop()

    def __repr__(self):
        return self.name

class SA:
    def __init__(self, type, thing, x = 0, y = 0):
        self.type = type
        self.thing = thing
        if self.type == "tilt":
            self.x = x
            self.y = y

class Frame:
    def __init__(self, *sas):
        self.subs = sas

# Some basic actions
# Incomplete
wavedash = Action("Wavedash", (Frame(SA("press", "X"), SA("tilt", "MAIN", 0.5, 1)),
                               Frame(),
                               Frame(SA("release", "X")),
                               Frame(),
                               Frame(SA("press", "R")),
                               Frame(),
                               Frame(SA("release", "R"), SA("tilt", "MAIN", 0.5, 0.5))))

nudgeLeft = Action("Nudge Left", (Frame(SA("tilt", "MAIN", 0.4, 0.5)),
                                  Frame()))