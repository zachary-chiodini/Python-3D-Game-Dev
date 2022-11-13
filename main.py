from numpy import array, int8
from pygame import display, init
from pygame.time import Clock


class Render:
    
    def __init__(self, frame_rate: int8 = int8(0), width: int8 = int8(0), height: int8 = int8(0)):
        self.frame_rate = frame_rate
        self.resolution = array([width, height], dtype=int8)
        self.display = display.set_mode(self.resolution)
        self.clock = Clock()
        init()


if __name__ == '__main__':
    Render()
    pass
