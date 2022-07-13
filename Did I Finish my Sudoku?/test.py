

# first solution

import numpy as np


def done_or_not(board):

    for x in range(9):
        if (
            # Rows
            len(set(board[x])) < 9 or
            # Columns
            len(set(board[a][x] for a in range(9))) < 9 or
            # Regions
            len(set(board[x//3*3+a//3][x//3*3+a % 3] for a in range(9))) < 9
        ):

            return "Try again!"

    return "Finished!"


# second solution


def done_or_not(aboard):  # board[i][j]
    board = np.array(aboard)

    rows = [board[i, :] for i in range(9)]
    cols = [board[:, j] for j in range(9)]
    sqrs = [board[i:i+3, j:j+3].flatten() for i in [0, 3, 6]
            for j in [0, 3, 6]]

    for view in np.vstack((rows, cols, sqrs)):
        if len(np.unique(view)) != 9:
            return 'Try again!'

    return 'Finished!'


# third solution


correct = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def done_or_not(board):
    # check rows
    for row in board:
        if sorted(row) != correct:
            return "Try again!"

    # check columns
    for column in zip(*board):
        if sorted(column) != correct:
            return "Try again!"

    # check regions
    for i in range(3):
        for j in range(3):
            region = []
            for line in board[i*3:(i+1)*3]:
                region += line[j*3:(j+1)*3]

            if sorted(region) != correct:
                return "Try again!"

    return "Finished!"
