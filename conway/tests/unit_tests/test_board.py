"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from conway import Board, Cell, Row, Size


def test_we_can_create_a_board():
    """We want to create a simple 3 * 3 board that defaults to dead cells"""
    board = Board(0, Size(3, 3))

    for r in range(board.rows):
        for j in range(board.cols):
            assert str(board[r][j]) == "."


def test_we_can_create_a_row():
    """We want to create a row with dead cells"""
    row = Row(3)

    for c in range(row.cols):
        assert str(row[c]) == "."


def test_we_can_read_a_cell():
    """A cell needs to display a dead cell by default"""
    cell = Cell(".")

    assert str(cell) == "."


def test_a_board_has_a_gen_identifier():
    """A board has a generatio"""
    board = Board(0, Size(3, 3))
    assert board.generation == 0


def test_a_size_has_two_dimensions():
    """A size tells us the dimensions of the board"""
    size = Size(3, 4)
    size.rows = 3
    size.cols = 4


def test_render_a_board():
    """We want to render a board, which is a good way to check it"""
    board = Board(0, Size(3, 4))
    expected_board = ("Generation 0\n"
                      "3 4\n"
                      "....\n"
                      "....\n"
                      "....\n"
                      )

    assert expected_board == str(board)


def test_render_a_row_with_four_cols():
    """We should produce 4 dead cells from a default row with 4 columns"""
    row = Row(4)
    expected_row = "...."

    assert expected_row == str(row)


def test_render_a_row_with_five_cols():
    """We should produce 5 dead cells rom a default row with 5 columns"""
    row = Row(5)
    expected_row = "....."

    assert expected_row == str(row)

# Test that a cell can be live too
