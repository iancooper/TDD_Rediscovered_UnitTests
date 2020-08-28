"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from typing import Any

class Board:
    def __init__(self, generation:int, size:'Size'):
        self.rows = size.rows
        self.cols = size.cols
        self.generation = generation

        self ._rows = [Row(self.cols) for n in range(self.rows)]

    def __getitem__(self, key):
        return self._rows[key]

    def __str__(self):
        view = []
        view.append(f"Generation {self.generation}")
        view.append(str(Size))
        for r in range(self.rows):
            grid.append(str(self[r]))

class Size:
    def __init__(self, rows: int, cols:int):
        self.rows = rows
        self.cols = cols

    def __str__(self):
        pass

class Row:
    def __init__(self, cols: int):
        self.cols = cols
        self._cells = [Cell() for n in range(self.cols)]

    def __getitem__(self, key):
        return self._cells[key]

    def __str__(self):
        return "".join("." for i in range(self.cols))

class Cell:
    def __str__(self):
        return "."


