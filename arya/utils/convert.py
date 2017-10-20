import os


def a(b):
    return int(b, 16)

while True:
    value = a(input())
    os.system("echo '%s' | pbcopy" % value)
    print("int:", value)
    
