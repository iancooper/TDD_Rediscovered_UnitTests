"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
from conway.ticker import tick


def test_a_grid_with_a_single_cell_dies(fake_board):
    board = fake_board[0]
    cells = fake_board[1]
    cells[1][1] = "*"

    def get_neighbours(row, col):
        """This will get us the neighbour count for a cell
            Assume that the board is 3 * 3 with a live cell at 1,1
            It has no neigbours, and dies
        """
        return 0

    board.get_live_neigbour_count = get_neighbours

    new_board = tick(board)

    assert str(new_board[1][1]) == "."


def test_a_cell_with_two_neighbours_lives(fake_board):
    board = fake_board[0]
    cells = fake_board[1]
    cells[0][1] = "*"
    cells[1][1] = "*"
    cells[2][1] = "*"

    def get_neighbours(row, col):
        """This will get us the neighbour count for a cell
            Assume that the board is 3 * 3 with a live cell at 1,1
            It has no neigbours, and dies
        """
        if row == 1 and col ==1:
            return 2
        elif col == 1:
            return 1
        else:
            return 0

    board.get_live_neigbour_count = get_neighbours

    new_board = tick(board)

    assert str(new_board[0][1]) == "."
    assert str(new_board[1][1]) == "*"
    assert str(new_board[2][1]) == "."

def test_a_cell_with_two_or_three_neighbours_lives(fake_board):
    board = fake_board[0]
    cells = fake_board[1]
    cells[0][1] = "*"
    cells[1][0] = "*"
    cells[1][1] = "*"
    cells[1][2] = "*"
    cells[2][1] = "*"

    def get_neighbours(row, col):
        """This will get us the neighbour count for a cell
            Assume that the board is 3 * 3 with a live cell at 1,1
            It has no neigbours, and dies
        """
        if row == 0:
            if col == 1:
                return 3
        elif row == 1:
            if col == 0 or col == 2:
                return 3
            else:
                return 4
        elif row == 2:
            if col == 1:
                return 3

        return 0

    board.get_live_neigbour_count = get_neighbours

    new_board = tick(board)

    assert str(new_board[0][1]) == "*"
    assert str(new_board[0][1]) == "*"
    assert str(new_board[1][1]) == "."
    assert str(new_board[1][2]) == "*"
    assert str(new_board[2][1]) == "*"

# test to prove that when you are surrounded by x live cells and are dead you wake up

def test_a_dead_cell_with_three_live_neighbours_lives(fake_board):
    board = fake_board[0]
    cells = fake_board[1]
    cells[1][0] = "*"
    cells[1][2] = "*"
    cells[2][1] = "*"

    def get_neighbours(row, col):
        """This will get us the neighbour count for a cell
            Assume that the board is 3 * 3 with a live cell at 1,1
            It has no neigbours, and dies
        """
        if row == 1:
            if col == 1:
                return 3
            if col == 2:
                return 1
        if row == 2:
            if col == 1:
                return 1

        return 0

    board.get_live_neigbour_count = get_neighbours

    new_board = tick(board)

    assert str(new_board[1][0]) == "."
    assert str(new_board[1][1]) == "*"
    assert str(new_board[1][2]) == "."
    assert str(new_board[2][1]) == "."
