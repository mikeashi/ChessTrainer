import chess
from Core.node import Node


class Tree:
    root: Node = None

    def __init__(self, board: chess.Board):
        self.root = Node(board)
