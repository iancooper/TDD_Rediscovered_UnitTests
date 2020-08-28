"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from typing import Any

class Board:
    def __init__(self, rows:int, cols:int):
        self.rows = rows
        self.cols = cols

        self ._rows = [Row(cols) for n in range(self.rows)]

    def __getitem__(self, key):
        return self._rows[key]

class Row:
    pass


