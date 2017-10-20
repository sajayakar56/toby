# arya
A framework for reading Melee memory in the Dolphin emulator as well as sending pad inputs through UNIX Pipes.

# Features
- Threaded memory reader that dumps any memory values received into a database
- Pad input writer that submits inputs through UNIX Pipes

# Setup Instructions
Tested only with Dolphin 5.0-5681
- Enable Netplay Community Settings!
- /MemoryWatcher/MemoryWatcher (run mkfifo MemoryWatcher here)
- Put Locations.txt -> MemoryWatcher/Locations.txt
- Create Pipes/arya (mkfifo arya)

# Credits 
spxtr's MemoryWatcher within Dolphin

spxtr/p3

altf4/SmashBot

vladfi1/phillip
