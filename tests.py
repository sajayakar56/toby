from MemoryManager import MemoryManager
import os

# Testing Memory Manager
def mem_test():
    x = MemoryManager()
    prev = None
    while True:
        data = str(x)
        if data and prev != data:
            prev = data
            os.system("clear")
            print(data)
            
mem_test()
