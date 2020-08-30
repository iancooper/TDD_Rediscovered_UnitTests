"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from conway import Board, Cell, Row, Size
from mock import Mock


def test_we_can_create_a_board():
    """We want to create a simple 3 * 3 board that defaults to dead cells"""
    row = Mock(Row)
    cell = Mock(Cell)
    cell.__str__ = Mock()
    cell.__str__.return_value = "."

    def get_item(key):
        return cell

    row.__getitem__ = Mock()
    row.__getitem__.side_effect = get_item

    board = Board(0, Size(3, 3), [row, row, row])

    for r in range(board.rows):
        for j in range(board.cols):
            assert str(board[r][j]) == "."


    assert cell.__str__.call_count == 9


def test_we_can_create_a_row():
    """We want to create a row with dead cells"""
    cell = Mock(Cell)
    cell.__str__ = Mock()
    cell.__str__.return_value = "."

    row = Row(3, [cell, cell, cell])

    for c in range(row.cols):
        assert str(row[c]) == "."

    assert cell.__str__.call_count == 3


def test_we_can_read_a_cell():
    """A cell needs to display a dead cell by default"""
    cell = Cell(".")

    assert str(cell) == "."


def test_a_board_has_a_gen_identifier():
    """A board has a generatio"""
    board = Board(0, Size(3, 3), [row_one, row_two, row_three])
    assert board.generation == 0


def test_a_size_has_two_dimensions():
    """A size tells us the dimensions of the board"""
    size = Size(3, 4)
    size.rows = 3
    size.cols = 4


def test_render_a_board():
    """We want to render a board, which is a good way to check it"""
    row = Mock(Row)
    cell = Mock(Cell)
    cell.__str__ = Mock()
    cell.__str__.return_value = "."

    def get_item(key):
        return cell

    row.__getitem__ = Mock()
    row.__getitem__.side_effect = get_item

    board = Board(0, Size(3, 4), [row, row, row])
    expected_board = ("Generation 0\n"
                      "3 4\n"
                      "....\n"
                      "....\n"
                      "....\n"
                      )

    assert expected_board == str(board)


def test_render_a_row_with_four_cols():
    """We should produce 4 dead cells from a default row with 4 columns"""
    cell = Mock(Cell)
    cell.__str__ = Mock()
    cell.__str__.return_value = "."

    row = Row(4, [cell, cell, cell, cell])
    expected_row = "...."

    assert expected_row == str(row)
    assert cell.__str__.call_count == 4


def test_render_a_row_with_five_cols():
    """We should produce 5 dead cells rom a default row with 5 columns"""
    cell = Mock(Cell)
    cell.__str__ = Mock()
    cell.__str__.return_value = "."

    row = Row(5, [cell, cell, cell, cell, cell])
    expected_row = "....."

    assert expected_row == str(row)
    assert cell.__str__.call_count == 5

