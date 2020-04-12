from unittest import TestCase
from Core.node import Node


class TestNode(TestCase):
    def test_search(self):
        root = Node.from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        d4 = Node.from_fen("rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1")
        d5 = Node.from_fen("rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2")
        c4 = Node.from_fen("rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2")
        e6 = Node.from_fen("rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3")
        nc3 = Node.from_fen("rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 3")

        e6.children.append(nc3)
        c4.children.append(e6)

        d5.children.append(c4)
        d4.children.append(d5)

        e4 = Node.from_fen("rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1")

        root.children.append(d4)
        root.children.append(e4)

        self.assertEqual(root.search(nc3.board), nc3)
