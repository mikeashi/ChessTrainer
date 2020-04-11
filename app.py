import chess


class App:

    def __init__(self, board):
        self.board = board

    @classmethod
    def start(cls):
        return cls(chess.Board())

    @classmethod
    def start_from_position(cls, position):
        return cls(chess.Board(position))