import os
home = os.path.expanduser("~")
dolphin = home + "/Library/Application Support/Dolphin"

# Move Locations.txt
print("Writing Locations.txt...")
LOCATIONS = open("Locations.txt", "r")
data = LOCATIONS.read()
LOCATIONS.close()
FILE = open(dolphin + "/MemoryWatcher/Locations.txt", "w")
FILE.write(data)
FILE.close()

# Check if pipe at MemoryWatcher exists, and create it otherwise
# TODO: I don't think this works
if not os.path.isfile(dolphin + "/MemoryWatcher/MemoryWatcher"):
    print("Creating MemoryWatcher pipe...")
    os.system("mkfifo " + dolphin + "/MemoryWatcher/MemoryWatcher")

# Install the padfile 
print("Writing GameCube controller config...")
CONFIG = open("gc_profile.ini", "r")
data = CONFIG.read()
CONFIG.close()
FILE = open(dolphin + "/Config/Profiles/GCPad/gc_profile.ini", "w")
FILE.write(data)
FILE.close()

# Create the pad pipe /Pipes/arya; probably have to make the folder
