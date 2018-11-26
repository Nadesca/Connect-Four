# -*- coding: utf8 -*-

__author__ = 'Nadia Cullmann'

# Dieses Programm simuliert ein Vier Gewinnt Spiel

import locale

locale.setlocale(locale.LC_ALL, 'de-DE')


def create_board():
    board = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
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


def get_horizontal_arrays():
    horizontal_arrays = list(board)
    horizontal_arrays.reverse()
    print("horizontal arrays: " + str(horizontal_arrays))
    return horizontal_arrays


def get_vertical_arrays():
    vertical_arrays = []
    temp_array = []
    for y in range(0, 7):
        for x in range(0, 6):
            temp_array.append(board[x][y])
        print(temp_array)
        vertical_arrays.append(temp_array)
        temp_array = []
            # reversed_board = board[::-1]
            # print(reversed_board)
    print("vertical arrays: " + str(vertical_arrays))
    return vertical_arrays


# def get_positive_diagonal_arrays2():
#     positive_diagonal_arrays = []
#     temp_array = []
#     for col in range(4):
#         for row in range(3):
#             for index in range(7):
#                 if (col + index) < 7 and (row + index) < 6:
#                     temp_array.append(board[row + index][col + index])
#             positive_diagonal_arrays.append(temp_array)
#             temp_array = []
#     print("positively sloped diagonal arrays: " + str(positive_diagonal_arrays))
#     return positive_diagonal_arrays
#
#
# def get_positive_diagonal_arrays():
#     elements2 = []
#     board.reverse()
#     for y in range(0, len(board)):
#         elements2.append([])
#         for x in range(y, -1, -1):
#             elements2[y].append(board[x][y - x])
#     for l in range(0, len(board[0])-1, 1):
#         elements2.append([])
#         for k in range(len(board)-1,-1,-1):
#             if len(board)-k+l < len(board[0]):
#                 elements2[len(board)+l].append(board[k][len(board)-k+l])
#     print(elements2)
#     board.reverse()
#     return elements2


def get_start_down(x, y):  # get upper start-point of negatively sloped diagonal through given point
    while x > 0 and y < len(board) - 1:
        x -= 1
        y += 1
    return x, y


def get_diag_down(x, y):  # iterate over negatively sloped diagonal downwards from starting-point and write values into array
    diag_down = []
    start_x, start_y = get_start_down(x, y)
    print("start x={},start y={}".format(start_x, start_y))
    while start_x < len(board[0]) - 1 and start_y < len(board) - 1:
        # print("x={0}y={1}".format(x, y))
        diag_down.append(board[start_x][start_y])
        start_x += 1
        start_y -= 1
    return diag_down


def get_start_up(current_row, current_col): # get lowest point of positive diagonal going through given point

     while  current_col > 0 and current_row > 0:
         current_col -= 1
         current_row -= 1
     return current_row, current_col


def get_diag_up(current_row, current_col): # iterate over positive diagonal from lowest point and write values into array
    diag_up = []
    start_y, start_x = get_start_up(current_row, current_col)
    print("start x={},start y={}".format(start_x, start_y))
    while start_x < len(board[0]) and start_y < len(board):
        # print("x={0}y={1}".format(x, y))
        # print(board[start_x][start_y])
        diag_up.append(board[start_y][start_x])
        start_x += 1
        start_y += 1
        print(start_x, start_y)
    return diag_up



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
    # counter = 0
    # for row in range(row_count):
    #     if board[row][current_col] == turn + 1:
    #         counter += 1
    #     elif board[row][current_col] == 0 and counter == 3:
    #         print("Player " + str(turn + 1) + " hat vertikalen threat in spalte " + str(current_col) + "!!")
    #         num_threats += 1
    #         counter = 0
    #         break
    #     else:
    #         counter = 0
    # check for horizontal threat:
    # counter = 0
    # for col in range(column_count):
    #     if board[current_row][col] == turn + 1:
    #         counter += 1
    #     elif counter == 3 and board[current_row][col] == 0:
    #         print("Player " + str(turn + 1) + " hat horizontalen threat in Position " + str(col) + "-" + str(
    #             current_row) + " !!")
    #         num_threats += 1
    #         counter = 0
    #         break
    #     else:
    #         counter = 0
    #     # loop backwards through same column
    # counter = 0
    # for col in range(column_count - 1, -1, -1):
    #     if board[current_row][col] == turn + 1:
    #         counter += 1
    #     elif counter == 3 and board[current_row][col] == 0:
    #         print("Player " + str(turn + 1) + " hat horizontalen threat in Position " + str(col) + "-" + str(
    #             current_row) + " !!")
    #         num_threats += 1
    #         counter = 0
    #         break
    #     else:
    #         counter = 0
    # check for positively sloped diagonal threat:
    counter = 0
    for col in range(4):
        for row in range(3):
            for index in range(7):
                if (col + index) < 7 and (row + index) < 6:
                    # print(str(col + index) + "/" + str(row + index))
                    if board[row + index][col + index] == (turn + 1):
                        # print(str(col + index) + "/" + str(row + index))
                        counter += 1
                    elif board[row + index][col + index] == 0 and counter == 3:
                        print("Player " + str(turn + 1) + " hat positiven diagonalen threat in Position " + str(
                            col + index + 1) + "-" + str(row + index + 1) + "!")
                        num_threats += 1
                        counter = 0
                    else:
                        counter = 0
                else:
                    break

     # check for free space at the other end of diagonal
    free_space_counter = 0
    counter = 0
    for col in range(4):
        for row in range(3):
            for index in range(0, 4):
                if index > 0 and board[row + index][col + index] == (turn + 1) and board[row + index - 1][col + index - 1] == 0:
                    free_space_counter = 1
                    counter = 1
                elif free_space_counter == 1 and counter == 2 and board[row + index][col + index] == (turn + 1):
                    counter += 1
                    print("Player " + str(turn + 1) + " hat positiven diagonalen threat in Position " + str(
                    col + index - 3) + "-" + str(row + index - 3) + "(vorne)!!")
                    num_threats += 1
                    counter = 0
                    free_space_counter = 0
                    break
                elif free_space_counter > 0 and counter > 0 and board[row + index][col + index] == (turn + 1):
                    counter += 1
                else:
                    counter = 0
                    free_space_counter = 0

    # check for negatively sloped diagonal threat:
    # counter = 0
    # for col in range(4):
    #     for row in range(3, row_count):
    #         for index in range(0, 4):
    #             if board[row - index][col + index] == (turn + 1):
    #                 counter += 1
    #             elif board[row - index][col + index] == 0 and counter == 3:
    #                 print("Player " + str(turn + 1) + " hat negativen diagonalen threat in Position " + str(
    #                     col + index) + "-" + str(row + index) + "!!")
    #                 num_threats += 1
    #                 counter = 0
    #                 break
    #             else:
    #                 counter = 0
    # # check for free space at the other end of diagonal
    # counter = 0
    # free_space_counter = 0
    # for col in range(4):
    #     for row in range(3, row_count):
    #         for index in range(0, 4):
    #             if (0 < index < 3) and board[row - index][col + index] == 0 and board[row - index - 1][col + index + 1] == (turn + 1):
    #                 free_space_counter += 1
    #             elif board[row - index][col + index] == (turn + 1) and free_space_counter > 0:
    #                 counter += 1
    #                 print("!!Player " + str(turn + 1) + " hat negativen diagonalen threat in Position " + str(
    #                     col + index) + "-" + str(row + index) + "!!")
    #                 num_threats += 1
    #                 counter = 0
    #                 free_space_counter = 0
    #                 break
    #             else:
    #                 counter = 0
    #                 free_space_counter = 0

    if num_threats > 0:
        return num_threats


game_over = False
turn = 0

while not game_over:
    # Ask for Player 1 Input
    # get_vertical_arrays()
    get_horizontal_arrays()
    # get_positive_diagonal_arrays()

    if turn == 0:
        valid_entry_player_1 = False
        while not valid_entry_player_1:
            choice_player1 = input("Player 1 bitte wähle eine Spalte(1-7)\n")
            try:
                current_col = int(choice_player1) - 1
                if current_col < 0 or current_col > 6:
                    print("Keine gültige Spaltenzahl!")
                    continue
                if is_valid_location(board, current_col):
                    current_row = get_next_open_row(board, current_col)
                    drop_piece(board, current_row, current_col)
                    draw_board()
                    print("board:" + str(board))
                    valid_entry_player_1 = True
                if check_for_winning_move(board, current_row, current_col, turn):
                    game_over = True
                if check_game_over(board):
                    game_over = True
                num_threats = has_threat(board, current_row, current_col, turn)
                get_diag_up(current_col, current_row)
                # print("diagthreat" + str(get_diag_down(current_col, current_row)))
                print("Anzahl neue threats: " + str(num_threats))
                print("start up" + str(get_start_up(current_col, current_row)))
                print("diagonals up" + str(get_diag_up(current_col, current_row)))
                # print("diag down" + str(diag-down-threat))

                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue

    # Ask for Player 2 Input
    if turn == 1:
        valid_entry_player_2 = False
        while not valid_entry_player_2:
            choice_player2 = input("Player 2 bitte wähle eine Spalte(1-7)\n")
            try:
                current_col = int(choice_player2) - 1
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
                    # print("diagthreat" + str(get_diag_down(current_col, current_row)))
                    print("start up" + str(get_start_up(current_col, current_row)))
                    print("diagonals up" + str(get_diag_up(current_col, current_row)))
                break
            except ValueError:
                print("Keine gültige Spaltenzahl!")
                continue
    turn += 1
    turn = turn % 2




