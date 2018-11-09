import sys
sys.path.insert(0,"C:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Lib\site-packages")
import numpy as np
import pandas as pd
from pandas import DataFrame
import pgzrun


playboard = Rect((50, 50), (700, 600))
WIDTH = playboard.width + 100
HEIGHT = playboard.height + 100


class Disc(object):

    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.pos = x, y
        self.image = image
        self.new_disc = Actor(image)
        self.new_disc.pos = x, y

    def draw(self):
        self.new_disc.draw()

    def update(self):
        if self.new_disc.y < 600:
            self.new_disc.y += 100
            self.new_disc.draw()


def draw():
    for disc in disc_collection:
        disc.draw()


def update():
    for disc in disc_collection:
        # screen.clear()
        disc.update()


disc_collection = []
disc_collection.append(Disc(100, 0, "red"))
disc_collection.append(Disc(200, 0, "yellow"))


pgzrun.go()
