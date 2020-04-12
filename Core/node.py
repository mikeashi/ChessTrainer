import chess

from Helpers.board_helper import BoardHelper


class Node:
    def __init__(self, board: chess.Board, parent=None):
        self.board = board
        self.hash = BoardHelper.hash(board)
        self.children = []
        self.parent = parent

    def search(self, board: chess.Board):
        if BoardHelper.hash(board) == self.hash:
            return self
        for child in self.children:
            tmp = child.search(board)
            if tmp is not None:
                return tmp
        return None

    @classmethod
    def from_fen(cls, fen, parent=None):
        return cls(chess.Board(fen), parent)
