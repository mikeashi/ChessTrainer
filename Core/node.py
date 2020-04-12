import chess

from Helpers.board_helper import BoardHelper


class Node:
    def __init__(self, board: chess.Board, move: chess.Move, parent):
        self.board = board
        self.move = move
        self.hash = BoardHelper.hash(board)
        self.children = []
        self.parent = parent


    def get_path(self):
        if self.parent is not None:
            parent_move = self.parent.get_path()
            if parent_move is not None:
                return self.parent.get_path() + '->' + self.move.uci()
            else:
                return self.move.uci()