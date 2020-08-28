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

    def __getitem__(self, key):
        return []
