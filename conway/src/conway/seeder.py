"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""
from typing import Tuple
from conway import Board, Size

class Seeder:

    def __init__(self, board: Board):
        self._board = board

    def generate_board(self, size: Size, *args: Tuple[int, int]) -> None:
        for arg in args:
            self._board[arg[0]][arg[1]] = "*"

