# ARYA
# Python Interface for reader and writer
# to interface with SSBM
# Stephen Jayakar
##########################################
from reader import Reader
from writer import Writer
import time

class Arya:
    def __init__(self):
        self.r = Reader()
        self.w = Writer()
        self.update_loop()

    def update_loop(self):
        frames = []
        prev_frame = None
        frame = None
        prev_time = time.time()
        while len(frames) < 1000:
            self.r.update()
            frame = self.r.state.frame
            # Means the frame has advanced
            if (frame != prev_frame):
                curr_time = time.time()
                frames.append(1/(curr_time - prev_time))
                prev_time, prev_frame = curr_time, frame
        lst = (sum([(x - 60)**2 for x in frames]) / 1000)
        self.x = sum([1 for x in frames if abs(60 - x) > 2])
        


if __name__ == "__main__":
    a = Arya()
    print(a.x)
