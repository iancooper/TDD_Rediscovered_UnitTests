"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from pytest_bdd import given, then, scenario, parsers


@scenario(
    'cross_game.feature',
    'Seed with five live cells in a cross shape'
)
def test_cross_game():
    pass

@given(parsers.parse('I have a board with:\n{board}'))
def i_have_a_board(board):
    return board

@then(parsers.parse('I expect the board to evolve to:\n{expected_board}'))
def board_should_match(i_have_a_board, board, expected_board)
    return board == expected_board


