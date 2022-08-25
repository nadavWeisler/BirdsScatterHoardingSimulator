from PyQt6.QtWidgets import QFrame, QGridLayout, QWidget

from utils import generate_matrix, getFakeAddress, rgb2hex


class Map:
    def __init__(self) -> None:
        super().__init__()
        self.name = getFakeAddress()
        self.matrix = generate_matrix()
        self.board = Board(self.matrix)


class Board(QFrame):
    def __init__(self, matrix):
        super().__init__()
        self.existingPlaces = {}
        self.setContentsMargins(0, 0, 0, 0)
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.draw_squares(matrix)
        self.setLayout(self.layout)

    def draw_squares(self, matrix):
        row_count = 0
        for row in matrix:
            col_count = 0
            for cell in row:
                square = QWidget(self)
                square.setStyleSheet(
                    'background-color: ' + rgb2hex(cell, cell, cell))
                self.layout.addWidget(square, row_count, col_count)
                col_count += 1
            row_count += 1

    def draw_food_place(self, x, y, color):
        currentKey = color + str(x) + str(y)
        if currentKey in self.existingPlaces.keys():
            if self.existingPlaces[currentKey].isHidden():
                self.existingPlaces[currentKey].show()
            else:
                self.existingPlaces[currentKey].hide()
        else:
            square = QWidget(self)
            square.setStyleSheet('background-color: ' + color)
            self.existingPlaces[currentKey] = square
            self.layout.addWidget(square, x, y)
