
# -*- coding: utf8 -*-

__author__ = 'Nadia Cullmann'

# Dieses Programm simuliert ein Vier Gewinnt Spiel

import locale

locale.setlocale(locale.LC_ALL, 'de-DE')


def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    return board


board = create_board()

row_count = 6
column_count = 7


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
    for row in range(row_count):
        if board[row][col] == 0:
            return row
            break


def drop_piece(board, row, col):
            board[row][col] = turn + 1


def check_game_over(board):
    for col in range(column_count):
        if board[5][col] == 0:
            return False
    print("Game Over!")
    return True


def check_for_winning_move(board, current_row, current_col, turn):
    # check for vertical win:
    counter = 0
    for row in range(row_count):
        if board[row][current_col] == (turn + 1):
            counter += 1
            if counter == 4:
                print("Player " + str(turn + 1) + " hat gewonnen!!")
                return True
        else:
            counter = 0

    # check_for_horizontal win:
    counter = 0
    for col in range(column_count):
        if board[current_row][col] == (turn + 1):
            counter += 1
            if counter == 4:
                print("Player " + str(turn + 1) + " hat gewonnen!!")
                return True
        else:
            counter = 0

    # check_for_positively sloped_diagonal:
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

    # check_for_negatively sloped_diagonal:
    counter = 0
    for col in range(4):
        for row in range(3, row_count):
            for index in range(0, 4):
                if board[row - index][col + index] == (turn + 1):
                    counter += 1
                    if counter == 4:
                        print("Player " + str(turn + 1) + " hat gewonnen!!")
                        return True
                else:
                    counter = 0


# check if player has a threat with current move:
def has_threat(board, current_row, current_col, turn):
    num_threats = 0
    # check for vertical threat:
    counter = 0
    for row in range(row_count):
        if board[row][current_col] == turn + 1:
            counter += 1
        elif board[row][current_col] == 0 and counter == 3:
            print("Player " + str(turn + 1) + " hat vertikalen threat in spalte " + str(current_col) + "!!")
            num_threats += 1
            counter = 0
            break
        else:
            counter = 0
    # check for horizontal threat:
    counter = 0
    for col in range(column_count):
        if board[current_row][col] == turn + 1:
            counter += 1
        elif counter == 3 and board[current_row][col] == 0:
            print("Player " + str(turn + 1) + " hat horizontalen threat in Position " + str(col) + "-" + str(current_row) + " !!")
            num_threats += 1
            counter = 0
            break
        else:
            counter = 0
        # loop backwards through same column
    counter = 0
    for col in range(column_count-1, -1, -1):
        if board[current_row][col] == turn + 1:
            counter += 1
        elif counter == 3 and board[current_row][col] == 0:
            print("Player " + str(turn + 1) + " hat horizontalen threat in Position " + str(col) + "-" + str(current_row) + " !!")
            num_threats += 1
            counter = 0
            break
        else:
            counter = 0
    # check for positively sloped diagonal threat:
    counter = 0
    for col in range(4):
        for row in range(3):
            for index in range(0, 4):
                if board[row + index][col + index] == (turn + 1):
                    counter += 1
                elif board[row + index][col + index] == 0 and counter == 3:
                    print("Player " + str(turn + 1) + " hat positiven diagonalen threat in Position" + str(col + index) + "-" +  str(row + index) + "!!")
                    num_threats += 1
                    counter = 0
                    break
                else:
                    counter = 0
                    # loop backwards through same diagonal
    counter = 0
    for col in range(4):
        for row in range(3):
            for index in range(3, -1, -1):
                if board[row + index][col + index] == (turn + 1):
                    counter += 1
                elif board[row + index][col + index] == 0 and counter == 3:
                    print("Player " + str(turn + 1) + " hat positiven diagonalen threat in Position " + str(col + index) + "-" + str(row + index) + "!!")
                    num_threats += 1
                    counter = 0
                    break
                else:
                    counter = 0
    # check for negatively sloped diagonal threat:
    counter = 0
    for col in range(4):
        for row in range(3, row_count):
            for index in range(0, 4):
                if board[row - index][col + index] == (turn + 1):
                    counter += 1
                elif board[row - index][col + index] == 0 and counter == 3:
                    print("Player " + str(turn + 1) + " hat negativen diagonalen threat in Position " + str(col + index) + "-" + str(row + index) + "!!")
                    num_threats += 1
                    counter = 0
                    break
                else:
                    counter = 0
    # check for free space at the other end of diagonal
    counter = 0
    free_space_counter = 0
    for col in range(4):
        for row in range(3, row_count):
            for index in range(0, 4):
                if 0 < index > 3 and board[row - index][col + index] == 0 and board[row - index - 1][col + index + 1] == (turn + 1):
                    free_space_counter += 1
                elif board[row - index][col + index] == (turn + 1) and free_space_counter > 0:
                    counter += 1
                    print("Player " + str(turn + 1) + " hat negativen diagonalen threat in Position " + str(
                        col + index) + "-" + str(row + index) + "!!")
                    num_threats += 1
                    counter = 0
                    free_space_counter = 0
                    break
                else:
                    counter = 0
                    free_space_counter = 0

    if num_threats > 0:
        return num_threats


game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    if turn == 0:
        valid_entry_player_1 = False
        while not valid_entry_player_1:
            current_col = input("Player 1 bitte wähle eine Spalte(0-6)\n")
            try:
                current_col = int(current_col)
                if current_col < 0 or current_col > 6:
                    print("Keine gültige Spaltenzahl!")
                    continue
                if is_valid_location(board, current_col):
                    current_row = get_next_open_row(board, current_col)
                    drop_piece(board, current_row, current_col)
                    draw_board()
                    valid_entry_player_1 = True
                if check_for_winning_move(board, current_row, current_col, turn):
                    game_over = True
                if check_game_over(board):
                    game_over = True
                num_threats = has_threat(board, current_row, current_col, turn)
                print("Anzahl neue threats: " + str(num_threats))

                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue

    # Ask for Player 2 Input
    if turn == 1:
        valid_entry_player_2 = False
        while not valid_entry_player_2:
            current_col = input("Player 2 bitte wähle eine Spalte(0-6)\n")
            try:
                current_col = int(current_col)
                if current_col < 0 or current_col > 6:
                    print("Keine gültige Spaltenzahl!")
                    continue
                if is_valid_location(board, current_col):
                    current_row = get_next_open_row(board, current_col)
                    drop_piece(board, current_row, current_col)
                    draw_board()
                    valid_entry_player_2 = True
                if check_for_winning_move(board, current_row, current_col, turn):
                    game_over = True
                if check_game_over(board):
                    game_over = True
                if not game_over:
                    num_threats = has_threat(board, current_row, current_col, turn)
                    print("Anzahl threats: " + str(num_threats))
                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue
    turn += 1
    turn = turn % 2



