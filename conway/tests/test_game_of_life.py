"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from conway import Board, Cell, Row


def test_we_can_create_a_board():
    board = Board(3, 3)

    for r in range(board.rows):
        for j in range(board.cols):
            assert str(board[r][j]) == "."


def test_we_can_create_a_row():
    row = Row(3)

    for c in range(row.cols):
        assert str(row[c]) == "."


def test_we_can_read_a_cell():
    cell = Cell()

    assert str(cell) == "."

# Test that a cell can be live too
