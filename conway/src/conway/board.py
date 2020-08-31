"""
Author: Ian Cooper
Date: 28 August 2020
Notes:
"""

from typing import Any, List


class Board:
    def __init__(self, generation: int, size: 'Size', rows: List['Row'] = None):
        self.rows = size.rows
        self.cols = size.cols
        self.generation = generation

        self._rows = rows or [Row(self.cols) for n in range(self.rows)]

    def __getitem__(self, key):
        return self._rows[key]

    def __str__(self):
        view = [f"Generation {self.generation}\n", str(Size(self.rows, self.cols)) + "\n"]
        for r in range(self.rows):
            view.append(str(self[r]) + "\n")
        return "".join(view)

    def get_live_neigbour_count(self, row: int, col:int):
        live_count = 0
        live_count += self._get_row_live_count(row -1, col)
        live_count += self._get_row_live_count(row, col, True)
        live_count += self._get_row_live_count(row +1, col)

        return live_count

    def _get_row_live_count(self, row: int, col: int, exclude: bool = False):
        """count the live cells in a row, in col and either side"""
        if row < 0 or row >= self.rows:
            return 0

        board_row = self._rows[row]

        live_count = 0
        if col -1 > 0 and board_row[col-1] == "*":
            live_count += 1
        if not exclude and board_row[col] == "*":
            live_count += 1
        if col + 1 < self.cols and board_row[col + 1] == "*":
            live_count += 1

        return live_count

class Size:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    def __str__(self):
        return f"{self.rows} {self.cols}"


class Row:
    def __init__(self, cols: int, cells: List['Cell'] = None):
        self.cols = cols
        self._cells = cells or [Cell('.') for n in range(self.cols)]

    def __getitem__(self, key):
        return self._cells[key]

    def __setitem__(self, key, value):
        self._cells[key] = value

    def __str__(self):
        view = []
        for i in range(self.cols):
            view.append(str(self._cells[i]))
        return "".join(view)


class Cell:
    def __init__(self, state: str):
        self._state = state

    def __str__(self):
        return self._state
