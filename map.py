from components.board import Board


class Map:
    def __init__(self, matrix) -> None:
        super().__init__()
        self.matrix = matrix
        self.board = Board(matrix)