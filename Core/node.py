import chess

from Helpers.board_helper import BoardHelper
import json


class Node(dict):
    def __init__(self, board: chess.Board, move: chess.Move, parent):
        self.board = board
        self.move = move
        self.hash = BoardHelper.hash(board)
        self.children = []
        self.parent = parent

    def to_json(self):
        """ Return a JSON representation of this node and all children. """
        return json.dumps(Node.encode_node(self))

    def get_path(self):
        if self.parent is not None:
            parent_move = self.parent.get_path()
            if parent_move is not None:
                return self.parent.get_path() + '->' + self.move.uci()
            else:
                return self.move.uci()

    @classmethod
    def with_children(cls, board: chess.Board, move: chess.Move, children):
        node = cls(board, move, None)
        node.children = children
        return node

    @staticmethod
    def encode_node(node):
        if node is None:
            return
        if node.move is None:
            move = ''
        else:
            move = node.move.uci()
        if len(node.children) > 0:
            children = []
            for child in node.children:
                children.append(Node.encode_node(child))
        elif len(node.children) == 1:
            children = node.children[0]
        else:
            children = None
        return {
            "fen": node.board.fen(),
            "move": move,
            "hash": node.hash,
            "children": children
        }

    @staticmethod
    def import_node(dict):
        board = chess.Board(dict['fen'])
        move = dict['move']
        children = []
        if dict['children'] is not None:
            if len(dict['children']) > 0:
                for child in dict['children']:
                    children.append(Node.import_node(child))
        return Node.with_children(
            board,
            move,
            children
        )
