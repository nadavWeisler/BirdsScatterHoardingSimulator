from colorsys import rgb_to_hls
from PyQt6.QtWidgets import QFrame, QGridLayout, QSizePolicy, QWidget
import numpy as np

from utils import rgb2hex


class Board(QFrame):
    def __init__(self, matrix):
        super().__init__()
        
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setContentsMargins(0, 0, 0, 0)

        self.layout = QGridLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.draw_squares(matrix)
        self.setLayout(self.layout)

    def draw_squares(self, matrix):
        row_count = 0
        for row in matrix:
            col_count = 0
            for cell in row:
                square = QWidget(self)
                square.setStyleSheet('background-color: ' + rgb2hex(cell, cell, cell))
                self.layout.addWidget(square, row_count, col_count)
                col_count += 1
            row_count += 1
