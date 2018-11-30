__author__ = 'Nadia Cullmann'


# Dieses Programm simuliert ein Vier Gewinnt Spiel

import locale
from tkinter import *


locale.setlocale(locale.LC_ALL, 'de-DE')


class Board:
    def __init__(self, row_count, col_count, active_player, matrix):
        self.row_count = row_count
        self.col_count = col_count
        self.active_player = active_player
        self.matrix = []

    def create_board(self, row_count, col_count):
        self.matrix

    def is_valid_location(self, current_col):
        if self.matrix[5][current_col] != 0:
            print("Die Reihe ist voll!")
        else:
            return True

    def get_next_open_row(self, current_col):
        for row in range(self.row_count):
            if self.matrix[row][current_col] == 0:
                return row
                break

"""

Main loop

"""

if __name__ == "__main__":

    root = Tk()


