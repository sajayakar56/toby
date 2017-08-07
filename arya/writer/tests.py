# Linked List tests (don't want to write bad data structs!)
from writer import LinkedList as ll

x = ll()
x.addLast(1)
x.addLast(2)
x.addLast(3)
print(x.removeFirst())
print(x.removeFirst())
print(x.removeFirst())
print(x.removeFirst())
x.addLast(4)
print(x.removeFirst())
print(x.removeFirst())
