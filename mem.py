from ctypes import *

# From StackOverflow Q#1592158
def hex_to_fp(s):
    s = s.strip("x\00")
    i = int(s, 16)
    cp = pointer(c_int(i))
    fp = cast(cp, POINTER(c_float))
    return fp.contents.value

# This doesn't work!
def hex_to_int(s):
    s = s.strip("x\00")
    s = s[::-1]
    i = int(s, 16)
    return i

class mem:
    def __init__(self, addr, name, t = "idk", hvalue = None):
        self.addr = addr
        self.name = name
        self.hvalue = hvalue
        self.t = t
        self.value = self.convert()

    def update(self, hvalue):
        self.hvalue = hvalue
        self.value = self.convert()

    def convert(self):
        if not self.hvalue:
            return None
        if (self.t == "float"):
            return hex_to_fp(self.hvalue)
        if (self.t == "int"):
            return hex_to_int(self.hvalue)
        else:
            return self.hvalue   
        
    def __repr__(self):
        return self.value

    def __str__(self):
        if self.value:
            return self.name + ": " + str(self.value)
        else:
            return self.name + ": "
