"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
from conway import Board, Size


def tick(board: Board):
    new_board = Board(board.generation + 1, Size(board.rows, board.cols))
    for r in range(board.rows):
        for c in range(board.cols):
            if board[r][c] == "*":
                live_count = board.get_live_neigbour_count(r, c)
                if live_count == 2 or live_count == 3:
                    new_board[r][c] = "*"
                else:
                    new_board[r][c] = "."
            else:
                live_count = board.get_live_neigbour_count(r, c)
                if live_count == 3:
                    new_board[r][c] = "*"
                else:
                    new_board[r][c] = "."
    return new_board
