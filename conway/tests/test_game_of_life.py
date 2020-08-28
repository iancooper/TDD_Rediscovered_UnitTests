"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from conway import Board

def test_we_can_create_a_board():
    board = Board(3, 3)

    assert board.rows == 3
    assert board.cols == 3





