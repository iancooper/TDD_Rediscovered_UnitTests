"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
from conway import Board
from conway.tick import tick
from mock import Mock, patch


def test_a_grid_with_a_single_cell_dies():
    board = Mock(Board)

    with patch(tick.Board) as test_board_class:
        board_instance = Mock()


        test_board_class.return_value = board_instance
        new_board = tick(board)


