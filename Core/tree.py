import chess
import chess.pgn

from Core.node import Node
from Helpers.board_helper import BoardHelper


class Tree:
    root: Node = None
    current: Node = None

    def __init__(self, board: chess.Board):
        self.root = Node(board)
        self.current = self.root

    def register_move(self, move: chess.Move):
        pseudo_board = BoardHelper.get_pseudo_board(self.current.board, move)
        node = self.root.search(pseudo_board)

        if node is not None:
            self.current = node
            return node

        node = Node(pseudo_board, self.current)

        self.current.children.append(node)
        self.current = node

    def back(self):
        if self.current == self.root:
            return
        self.current = self.current.parent

    def back_to_root(self):
        while self.current is not self.root:
            self.current = self.current.parent

    @classmethod
    def from_fen(cls, fen):
        return cls(chess.Board(fen))

    @classmethod
    def from_pgn(cls, pgn):
        # TODO check if pgn is None
        game = chess.pgn.read_game(pgn)
        for move in game.mainline_moves():
            print(move)
