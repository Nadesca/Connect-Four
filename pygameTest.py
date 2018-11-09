import sys
sys.path.insert(0,"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\site-packages")
import numpy as np
import pandas as pd
from pandas import DataFrame
import pgzrun


playboard = Rect((50, 50), (700, 600))
WIDTH = playboard.width + 100
HEIGHT = playboard.height + 100

# alien = Actor('alien')
# alien.pos = 100, 56
# alien.topright = 30, 30


def get_color():
    return "white"


class Board:
    def __init__(self, rows, cols):
        # self.create_board = Actor("board")
        self.rows = rows
        self.cols = cols


board = Board(6, 7)
DataFrame(np.zeros([6, 7]), index=range(5, -1, -1), dtype=int)


class Disc:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        screen.draw.filled_circle((self.x, self.y), 30, self.color)
        # screen.draw.filled_circle((700, 600), 30, 'red')

    def update(self):
        while self.y < 600:
            screen.draw.filled_circle((self.x, self.y), 30, "black")
            self.y = self.y + 100
            self.draw()


def draw():
    screen.clear()
    # draw board
    screen.draw.filled_rect(playboard, 'blue')
    for col in range(1, 8):
        for row in range(1, 7):
            screen.draw.filled_circle((col * 100, row * 100), 30, 'black')
    disc = Disc(100, 100, 'yellow')
    disc.draw()
    disc.update()

    # screen.draw.filled_circle((700, 600), 30, 'red')


pgzrun.go()

