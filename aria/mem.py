import struct

# For the conversion methods, must pass in bytes!
# From StackOverflow Q#1592158
def hex_to_fp(s):
    return struct.unpack(">f", s)[0]

# This doesn't work!
def hex_to_int(s):
    # Padding to length 4 (WHY DOESN'T IT COME THIS WAY)
    s = s.ljust(4, b'\0')
    return struct.unpack("<i", s)[0]

class mem:
    def __init__(self, t = "idk", hvalue = None):
        self.t = t
        self.update(hvalue)

    def update(self, hvalue):
        if hvalue and hvalue != "0\x00":
            self.hvalue = hvalue[0:-1]
            if (len(self.hvalue)%2):
                self.hvalue += "0"
            self.hvalue = bytes.fromhex(self.hvalue)
            self.value = self.convert()
        else:
            self.hvalue = None
            self.value = None

    def convert(self):
        if not self.hvalue:
            return None
        if (self.t == "f"):
            return hex_to_fp(self.hvalue)
        if (self.t == "i"):
            return hex_to_int(self.hvalue)
        else:
            return self.hvalue

    def val(self):
        return self.value

    def novalue(self):
        if self.t == "i":
            return 0
        if self.t == "f":
            return 0.0
        return "N/A"
        
