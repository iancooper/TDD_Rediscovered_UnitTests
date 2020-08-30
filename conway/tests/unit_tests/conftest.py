import pytest
from conway import Board, Size
from mock import Mock

@pytest.fixture
def board():
    board = Mock(Board)
    board.generation = 0
    board.rows = 3
    board.cols = 3
    return board

@pytest.fixture
def fake_board(board):
    cells = []
    for r in range(board.rows):
        line = []
        cells.append(line)
        for c in range(board.cols):
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
