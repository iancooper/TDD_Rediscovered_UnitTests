"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from mock import call, patch
from conway import Seeder, Size


def test_we_can_create_a_board_with_two_live_cells():
    """We have a seeder that is essentially a board factory; it makes a board of the appropriate size"""
    with patch("conway.Board", autospec=True) as board, patch("conway.Row", autospec=True) as row:
        board.size
        seeder = Seeder(board)
        seeder.generate_board((1, 1), (1, 2))
        board.assert_has_calls([call((1, 1)), call((1,2))], any_order=True)


