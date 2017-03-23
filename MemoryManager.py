from MemoryWatcher import MemoryWatcher
from os.path import expanduser
from mem import mem
home = expanduser("~")

class MemoryManager:
    table = {"00453090": mem("00453090", "P1 X", "float"),
             "00453094": mem("00453094", "P1 Y", "float"),
             "004530E0": mem("004530E0", "P1 %", "int"),
             "00453F20": mem("00453F20", "P2 X", "float"),
             "00453F24": mem("00453F24", "P2 Y", "float"),
             "00453F70": mem("00453F70", "P2 %", "int")}
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

    def __str__(self):
        self.update()
        string = ""
        for memory in self.table.values():
            string += str(memory) + "\n"
        return string
        
        
        
