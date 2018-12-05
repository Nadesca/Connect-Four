__author__ = 'Nadia Cullmann'


# Dieses Programm simuliert ein Vier Gewinnt Spiel

import locale
from tkinter import *


locale.setlocale(locale.LC_ALL, 'de-DE')


class Player:
    def __init__(self, is_first_player, player_name=None, color="default", is_human=True):
        self.is_first_player = is_first_player
        self.is_human = is_human
        self.color = color
        self._name = player_name
        if self.color == "default":
            if self.is_first_player:
                self.color = "yellow"
            else:
                self.color = "red"
        if player_name is None:
            if is_first_player:
                self._name = "Player One"
            else:
                self._name = "Player Two"
        else:
            chars = sum(c.isalpha() for c in str(
                player_name))  # check player name --> rules: no special characters including space, only numbers/letter, at least 3 letters, not used by another user
            if int(chars) < 3:
                raise Exception("Invalid name!")
                self._name = player_name
            else:
                self._name = player_name

    @property
    def name(self):
        print("getting value")
        return self._name

    @name.setter                   # rules: no special characters including space, only numbers/letter, at least 3 letters, not used by another user
    def name(self, value):
        chars = sum(c.isalpha() for c in str(value))
        print(chars)
        if self._name == "Player One" or "Player Two":
            if int(chars) < 3:
                raise Exception(print("Invalid name!"))
            self._name = value
        else:
            raise Exception("Can't rename Person")


class Board:
    def __init__(self, row_count, col_count, current_player):
        self.row_count = row_count
        self.col_count = col_count
        self.current_player = current_player  # boolean for player 0 or 1
        self.matrix = []
        for row in range(0, self.row_count):
            self.matrix.append([])
            for col in range(0, self.col_count):
                self.matrix[row].append(0)

    def draw_board(self):
        my_board = reversed(self.matrix)
        for row in my_board:
            print(row)
        # for row in self.matrix[::-1]:
        #     print(row)

    def get_current_player(self):
        return self.current_player

    def switch_player(self):
        self.current_player = not self.current_player

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

    def drop_piece(self, row, col):
        self.matrix[row][col] = (self.get_current_player() + 1)

    def check_if_winner(self, current_row, current_col):
        pass

    def check_if_game_over(self):
        pass

    def has_threat(self, current_row, current_col, turn):
        pass


"""
Main loop
"""

if __name__ == "__main__":

    root = Tk()
    board = Board(6, 7, 0)
    game_over = False
    turn = 0
    player1 = Player(True, "Nadia")
    player2 = Player(False)
    player2.name = "Leo"

    while not game_over:
        # Ask for Player 1 Input
        if board.get_current_player() == 0:
            print("Hallo " + str(player1._name))
            valid_entry_player_1 = False
            while not valid_entry_player_1:
                choice_player1 = input("Bitte wähle eine Spalte(0-6)\n")
                try:
                    current_col = int(choice_player1) - 1
                    if current_col < 0 or current_col > 6:
                        print("Keine gültige Spaltenzahl!")
                        continue
                    if board.is_valid_location(current_col):
                        current_row = board.get_next_open_row(current_col)
                        board.drop_piece(current_row, current_col)
                        board.draw_board()
                        valid_entry_player_1 = True
                    if board.check_if_winner(current_row, current_col):
                        game_over = True
                    if board.check_if_game_over():
                        game_over = True
                    num_threats = board.has_threat(current_row, current_col, turn)
                    print("Anzahl neue threats: " + str(num_threats))

                    break
                except ValueError:
                    print("Keine gültige Spaltenzahl!")
                    continue

        # Ask for Player 2 Input
        if board.get_current_player() == 1:
            print("Hallo " + str(player2._name))
            valid_entry_player_2 = False
            while not valid_entry_player_2:
                choice_player2 = input("Bitte wähle eine Spalte(0-6)\n")
                try:
                    current_col = int(choice_player2) - 1
                    if current_col < 0 or current_col > 6:
                        print("Keine gültige Spaltenzahl!")
                        continue
                    if board.is_valid_location(current_col):
                        current_row = board.get_next_open_row(current_col)
                        board.drop_piece(current_row, current_col)
                        board.draw_board()
                        valid_entry_player_2 = True
                    if board.check_if_winner(current_row, current_col):
                        game_over = True
                    if board.check_if_game_over():
                        game_over = True
                    if not game_over:
                        num_threats = board.has_threat(current_row, current_col, turn)
                        print("Anzahl threats: " + str(num_threats))
                    break
                except ValueError:
                    print("Keine gültige Spaltenzahl!")
                    continue
        board.switch_player()



