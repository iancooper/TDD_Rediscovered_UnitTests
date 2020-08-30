"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
from conway import Seeder, Size
from mock import call


def test_we_can_create_a_board_with_two_live_cells(fake_board):
    """We have a seeder that is essentially a board factory; it makes a board of the appropriate size"""
    board = fake_board[0]
    cells = fake_board[1]

    seeder = Seeder(board)

    seeder.generate_board(Size(board.rows, board.cols), (1, 1), (2, 2))

    board.__getitem__.assert_has_calls([call(1), call(2)], any_order=False)
    assert cells[1][1] == "*"
    assert cells[2][2] == "*"
