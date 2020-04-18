from json import JSONDecoder

import chess.pgn

from Core.node import Node
from Helpers.board_helper import BoardHelper


class Tree:
    root: Node = None
    current: Node = None

    def __init__(self, board: chess.Board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")):
        self.root = Node(board, None, None)
        self.current = self.root

    def register_move(self, move: chess.Move):
        for child in self.current.children:
            if child.move == move:
                self.current = child
                return
        new_board = BoardHelper.get_pseudo_board(self.current.board, move)
        node = Node(new_board, move, self.current)
        self.current.children.append(node)
        self.current = node

    def back(self):
        if self.current == self.root:
            return
        self.current = self.current.parent

    def back_to_root(self):
        while self.current is not self.root:
            self.current = self.current.parent

    def search(self, board: chess.Board):
        hash = BoardHelper.hash(board)
        stack = [self.root]
        result = []
        while True:
            tmp = stack.pop()
            if tmp.hash == hash:
                result.append(tmp)
            for child in tmp.children:
                stack.append(child)
            if len(stack) == 0:
                break
        return result

    def to_json(self):
        return self.root.to_json()

    def from_json(self, json):
        dict = JSONDecoder().decode(json)
        node = Node.import_node(dict)
        self.root = node
        self.current = node
        self.reset_parent(self.root)

    def reset_parent(self, node):
        stack = [node]
        while True:
            tmp = stack.pop()
            for child in tmp.children:
                child.parent = tmp
                stack.append(child)
            if len(stack) == 0:
                break
