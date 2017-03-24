from aria.MemoryWatcher import MemoryWatcher
from os.path import expanduser
from aria.mem import mem
home = expanduser("~")

class MemoryManager:
    alias = {"P1 X": "00453090",
             "P1 Y": "00453094",
             "P1 %": "004530E0",
             "P2 X": "00453F20",
             "P2 Y": "00453F24",
             "P2 %": "00453F70"}
             
    table = {"00453090": mem("f"),
             "00453094": mem("f"),
             "004530E0": mem("i"),
             "00453F20": mem("f"),
             "00453F24": mem("f"),
             "00453F70": mem("i")}
    keys = len(table.keys())
    path = "MemoryWatcher"
    def __init__(self):
        self.path = home + "/Library/Application Support/Dolphin/MemoryWatcher/" + self.path
        self.mw = MemoryWatcher(self.path)
        self.mw.__enter__()
    
    def update(self):
        data = next(self.mw)
        if data:
             m = self.table[data[0]]
             m.update(data[1])

    # Get the value of a "name" of an address
    def get(self, *args):
        self.update()
        vals = []
        for arg in args:
            addr = self.alias[arg]
            m = self.table[addr]
            vals.append(m.val())
        if len(vals) > 1:
            return vals
        else:
            return vals[0]

    def __str__(self):
        self.update()
        string = ""
        for key in self.alias.keys():
            string += key + ": " + self.get(key) + "\n"
        return string


        
        
        
