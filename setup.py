import os
home = os.path.expanduser("~")
dolphin = home + "/Library/Application Support/Dolphin"

# Move Locations.txt
print("Writing Locations.txt...")
LOCATIONS = open("Locations.txt", "r")
LOCATIONS = LOCATIONS.read()
FILE = open(dolphin + "/MemoryWatcher/Locations.txt", "w")
FILE.write(LOCATIONS)
FILE.close()

# Check if pipe at MemoryWatcher exists, and create it otherwise
if not os.path.isfile(dolphin + "/MemoryWatcher/MemoryWatcher"):
    print("Creating MemoryWatcher pipe...")
    os.system("mkfifo " + dolphin + "/MemoryWatcher/MemoryWatcher")
