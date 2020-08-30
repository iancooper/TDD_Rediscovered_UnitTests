"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
import pytest
from mock import call, patch, Mock, MagicMock
from conway import Board, Cell, Row, Seeder, Size

@pytest.fixture
def fake_board():
    board = Mock(Board)
    board_size = Size(3, 3)
    board.rows = Mock(int)
    board.rows.return_value = 3
    board.cols = Mock(int)
    board.cols.return_value = 3

    cells = []
    for r in range(board_size.rows):
        line = []
        cells.append(line)
        for c in range(board_size.cols):
            line.append(".")

    current_row = 0
    def get_row(key):
        nonlocal current_row
        current_row = key
        return cells[key]

    board.__getitem__ = Mock()
    board.__getitem__.side_effect = get_row

    board.__getitem__ = Mock()
    board.__getitem__.side_effect = get_row

    return (board, cells)


def test_we_can_create_a_board_with_two_live_cells(fake_board):
    """We have a seeder that is essentially a board factory; it makes a board of the appropriate size"""
    board = fake_board[0]
    cells = fake_board[1]

    seeder = Seeder(board)

    seeder.generate_board(Size(board.rows, board.cols), (1, 1), (2, 2))

    board.__getitem__.assert_has_calls([call(1), call(2)], any_order=False)
    assert cells[1][1] == "*"
    assert cells[2][2] == "*"

