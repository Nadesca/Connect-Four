
# -*- coding: utf8 -*-

__author__ = 'Nadia Cullmann'

# Dieses Programm simuliert ein Vier Gewinnt Spiel

import locale

locale.setlocale(locale.LC_ALL, 'de-DE')


def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return board


board = create_board()


def draw_board():
    for row in reversed(board):
        print(row)
    reversed(board)


def is_valid_location(board, col):
    if board[5][col] != 0:
        print("Die Reihe ist voll!")
    else:
        return True


def get_next_open_row(board, col):
    for row in range(len(board)):
        if board[row][col] == 0:
            return row
            break


def drop_piece(board, row, col):
            board[row][col] = turn + 1


def check_game_over(board):
    for col in range(len(board[0])):
        if board[5][col] == 0:
            return False
    print("Game Over!")
    return True


def check_for_winning_move(board, current_row, current_col, turn):
    # check for vertical win:
    if current_col > 2:
        counter = 0
        for row in range(len(board)):
            if board[row][current_col] == (turn + 1):
                counter += 1
                if counter == 4:
                    print("Player " + str(turn) + " hat gewonnen!!")
                    return True
            else:
                counter = 0

    # check_for_horizontal win:
    counter = 0
    for col in range(len(board[0])):
        if board[current_row][col] == (turn + 1):
            counter += 1
            if counter == 4:
                print("Player " + str(turn) + " hat gewonnen!!")
                return True
        else:
            counter = 0

    # check_for_positively sloped_diagonal in relevant places:
    if current_row < 3 and current_col < 4:
        counter = 0
        for col in range(4):
            for row in range(3):
                for index in range(0, 4):
                    if board[row + index][col + index] == (turn + 1):
                        counter += 1
                        if counter == 4:
                            print("Player " + str(turn + 1) + " hat gewonnen!!")
                            return True
                else:
                    counter = 0

    # check_for_negatively sloped_diagonal in relevant places:
    if current_row > 2 and current_col > 2:
        counter = 0
        for col in range(4):
            for row in range(3):
                for index in range(0, 4):
                    if board[row - index][col + index] == (turn + 1):
                        counter += 1
                        if counter == 4:
                            print("Player " + str(turn + 1) + " hat gewonnen!!")
                            return True
                else:
                    counter = 0


game_over = False
turn = 0


while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        while True:
            current_col = input("Player 1 bitte wähle eine Spalte(0-6)")
            try:
                current_col = int(current_col)
                if current_col < 0 or current_col > 6:
                    print("Keine gültige Spaltenzahl!")
                    continue
                if is_valid_location(board, current_col):
                    current_row = get_next_open_row(board, current_col)
                    drop_piece(board, current_row, current_col)
                    draw_board()
                if check_for_winning_move(board, current_row, current_col, turn):
                    game_over = True
                if check_game_over(board):
                    game_over = True
                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue

    # Ask for Player 2 Input
    if turn == 1:
        while True:
            current_col = input("Player 2 bitte wähle eine Spalte(0-6)")
            try:
                current_col = int(current_col)
                if current_col < 0 or current_col > 6:
                    print("Keine gültige Spaltenzahl!")
                    continue
                if is_valid_location(board, current_col):
                    current_row = get_next_open_row(board, current_col)
                    drop_piece(board, current_row, current_col)
                    draw_board()
                if check_for_winning_move(board, current_row, current_col, turn):
                    game_over = True
                if check_game_over(board):
                    game_over = True
                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue
    turn += 1
    turn = turn % 2


