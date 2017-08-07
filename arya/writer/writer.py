# from .Pad import *


class Writer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.p = Pad()
        self.frames = LinkedList()

    # will separate actions and frames, as well as run them in loop
    def parse(self, s: str) -> None:
        return None

    # will re-instantiate the linked list
    def clear(self) -> None:
        return None
        
    # Helper that actually performs one action
    def _do_action(self, s: str) -> None:
        s = s.split(" ")
        if s[0] == "r":
            if len(s) == 1:
                self.p.reset()
            else:
                button = s[1]
                assert button in dir(Button)
                self.p.release_button(Button[button])
        elif s[0] == "p":
            button = s[1]
            assert button in dir(Button)
            self.p.press_button(Button[button])
        elif s[0] == "t":
            x = float(s[2])
            y = float(s[3])
            self.p.tilt_stick(Stick[s[1]], x, y)
        elif s[0] == "tr":
            amt = float(s[2])
            self.p.press_trigger(Trigger[s[1]], amt)


# FIFO is the best way to handle the storage and execution of frames as data
class LinkedList:
    class Node:
        def __init__(self, item: str = None):
            self.item = item
            if item is not None:
                self.next = Node()
            else:
                self.next = None
            
    def __init__(self):
        self.first = LinkedList.Node()
        self.last = self.first
        self.size = 0

    def addLast(self, data: str) -> None:
        self.last.item = data
        self.last.next = LinkedList.Node()
        self.last = self.last.next
        self.size += 1

    def removeFirst(self) -> str:
        if self.size > 0:
            data = self.first.item
            self.first = self.first.next
            self.size -= 1
            return data
        return None
    
    def size(self) -> int:
        return self.size



    
    

