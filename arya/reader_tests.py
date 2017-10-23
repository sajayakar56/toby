from reader import Reader
import os
import time

prev_state = None
prev_time = time.time()

while True:
    r = Reader()
    r.update()
    state = r.state.frame
    if state != prev_state:
        print(state, prev_state)
        prev_state = state
        curr_time = time.time()
        print(1/(curr_time - prev_time))
        prev_time = curr_time
