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

    def debug_loop(self, frame_count: int):
        frames = []
        prev_frame = None
        frame = None
        prev_time = time.time()
        while len(frames) < frame_count:
            self.r.update()
            frame = self.r.state.frame
            # Means the frame has advanced
            if (frame != prev_frame):
                curr_time = time.time()
                frames.append(1/(curr_time - prev_time))
                prev_time, prev_frame = curr_time, frame
        lst = (sum([(x - 60)**2 for x in frames]) / frame_count)
        self.x = sum([1 for x in frames if abs(60 - x) > 2])
        


if __name__ == "__main__":
    a = Arya()
    a.debug_loop(600)
    print(a.x)
