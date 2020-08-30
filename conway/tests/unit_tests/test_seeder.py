"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from mock import call, patch, Mock, MagicMock
from conway import Board, Cell, Row, Seeder, Size


def test_we_can_create_a_board_with_two_live_cells():
    """We have a seeder that is essentially a board factory; it makes a board of the appropriate size"""
    board = Mock(Board)
    board_size = Size(3, 3)
    cell = Mock(Cell)
    row = Mock(Row)

    cells = []
    for r in range(board_size.rows):
        line = []
        cells.append(line)
        for c in range(board_size.cols):
            line.append(".")

    current_row = 0
    def get_row(key):
        current_row = key
        return cells[key]

    def set_cell(_, key, value):
        cells[current_row][key] = value

    row.__getitem__ = Mock()
    row.__getitem__.side_effect = get_row
    row.__setitem__ = Mock()
    row.__setitem__ = set_cell

    def get_row(key):
        return row

    board.__getitem__ = Mock()
    board.__getitem__.side_effect = get_row

    seeder = Seeder(board)

    seeder.generate_board(board_size, (1, 1), (2, 2))

    board.__getitem__.assert_has_calls([call(1), call(2)], any_order=False)
