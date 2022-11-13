from numpy import array
from pygame import display, init
from pygame.time import Clock


class Renderer:
    
    def __init__(self, frame_rate: int = 0, width: int = 0, height: int = 0):
        init()
        self.frame_rate = frame_rate
        self.resolution = (width, height)
        self.display = display.set_mode(self.resolution)
        self.clock = Clock()


if __name__ == '__main__':
    pass
