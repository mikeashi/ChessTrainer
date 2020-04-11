import chess.polyglot


class Node:
    def __init__(self, board: chess.Board):
        self.fen = board.board_fen()
        self.hash = chess.polyglot.zobrist_hash(board)
        self.children = []

    def search(self, wanted):
        if wanted == self.hash:
            return self
        for child in self.children:
            tmp = child.search(wanted)
            if tmp is not None:
                return tmp
        return None

    @classmethod
    def from_fen(cls, fen):
        return cls(chess.Board(fen))
