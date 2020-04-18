import copy
from unittest import TestCase

import chess

from Core.node import Node
from Core.tree import Tree
import json


class TestTree(TestCase):
    def setUp(self):
        self.tree = Tree()

    def test_register_a_new_move(self):
        self.register_move('e2e4')
        self.assertEqual(1, len(self.tree.root.children))

    def test_it_can_go_back_a_node(self):
        self.register_move('e2e4')
        self.tree.back()
        self.assertEqual(self.tree.root, self.tree.current)

    def test_it_can_go_back_to_root(self):
        self.register_move('e2e4')
        self.register_move('e7e5')
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.tree.back_to_root()
        self.assertEqual(self.tree.root, self.tree.current)

    def test_it_creates_a_new_variation(self):
        self.register_move('e2e4')
        self.tree.back_to_root()
        self.register_move('d2d4')
        self.assertEqual(2, len(self.tree.root.children))

    def test_register_does_not_create_a_new_variation_when_the_given_move_is_already_part_of_the_tree(self):
        self.register_move('e2e4')
        self.tree.back_to_root()
        self.register_move('e2e4')
        self.assertEqual(1, len(self.tree.root.children))

    def test_it_keeps_track_of_all_lines(self):
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.register_move('e2e4')
        self.register_move('e7e5')
        self.tree.back_to_root()

        self.register_move('e2e4')
        self.register_move('e7e5')
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.tree.back_to_root()

        self.register_move('d2d4')
        self.register_move('e7e5')
        self.register_move('e2e4')
        self.register_move('d7d5')
        self.tree.back_to_root()

        # root has two lines: the first starts with d4 and the other e4
        self.assertEqual(2, len(self.tree.root.children))
        # after d4 there is two lines: d5 and e5
        self.assertEqual(2, len(self.tree.root.children[0].children))
        # after e4 there is one line: e5
        self.assertEqual(1, len(self.tree.root.children[1].children))

    def test_search(self):
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.register_move('c2c4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        nc3 = self.tree.current

        self.tree.back_to_root()
        self.register_move('e2e4')

        self.assertEqual(self.tree.search(nc3.board), [nc3])

        self.tree.back_to_root()
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        nc3_2 = self.tree.current

        self.assertEqual(self.tree.search(nc3.board), [nc3_2, nc3])

        self.tree.back_to_root()
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('b1c3')
        nc3_3 = self.tree.current

        self.assertEqual(self.tree.search(nc3.board), [nc3_2, nc3_3, nc3])

    def test_export_json(self):
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.register_move('c2c4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        self.tree.back_to_root()
        self.register_move('e2e4')
        self.tree.back_to_root()
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        self.tree.back_to_root()
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('b1c3')
        self.assertEqual('{"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", "move": "", '
                         '"hash": 5060803636482931868, "children": [{"fen": '
                         '"rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1", "move": "d2d4", '
                         '"hash": 9443689642921087454, "children": [{"fen": '
                         '"rnbqkbnr/ppp1pppp/8/3p4/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2", "move": "d7d5", '
                         '"hash": 460664201775194104, "children": [{"fen": '
                         '"rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2", "move": "c2c4", '
                         '"hash": 9963937660605248767, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3", "move": "e7e6", '
                         '"hash": 18172295748331349165, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 3", "move": "b1c3", '
                         '"hash": 551671236195985012, "children": null}]}]}]}, {"fen": '
                         '"rnbqkbnr/pppp1ppp/4p3/8/3P4/8/PPP1PPPP/RNBQKBNR w KQkq - 0 2", "move": "e7e6", '
                         '"hash": 17688252038015238540, "children": [{"fen": '
                         '"rnbqkbnr/pppp1ppp/4p3/8/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2", "move": "c2c4", '
                         '"hash": 8744535441769097867, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3", "move": "d7d5", '
                         '"hash": 18172295748331349165, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 3", "move": "b1c3", '
                         '"hash": 551671236195985012, "children": null}]}]}]}]}, '
                         '{"fen": "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1", "move": "e2e4", '
                         '"hash": 9384546495678726550, "children": null}, {"fen": '
                         '"rnbqkbnr/pppppppp/8/8/2P5/8/PP1PPPPP/RNBQKBNR b KQkq - 0 1", "move": "c2c4", '
                         '"hash": 14562399549841627035, "children": [{"fen": '
                         '"rnbqkbnr/ppp1pppp/8/3p4/2P5/8/PP1PPPPP/RNBQKBNR w KQkq - 0 2", "move": "d7d5", '
                         '"hash": 5724685530517084605, "children": [{"fen": '
                         '"rnbqkbnr/ppp1pppp/8/3p4/2PP4/8/PP2PPPP/RNBQKBNR b KQkq - 0 2", "move": "d2d4", '
                         '"hash": 9963937660605248767, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3", "move": "e7e6", '
                         '"hash": 18172295748331349165, "children": [{"fen": '
                         '"rnbqkbnr/ppp2ppp/4p3/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR b KQkq - 1 3", "move": "b1c3", '
                         '"hash": 551671236195985012, "children": null}]}]}]}]}]}',
                         self.tree.root.to_json())

    def test_import_json(self):
        self.register_move('d2d4')
        self.register_move('d7d5')
        self.register_move('c2c4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        self.tree.back_to_root()
        self.register_move('e2e4')
        self.tree.back_to_root()
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('b1c3')
        self.tree.back_to_root()
        self.register_move('d2d4')
        self.register_move('e7e6')
        self.register_move('c2c4')
        self.register_move('d7d5')
        self.register_move('b1c3')
        tmp = copy.deepcopy(self.tree.root)
        self.tree.from_json(self.tree.to_json())
        self.assertEqual(tmp,self.tree.root)

    def register_move(self, move):
        self.tree.register_move(chess.Move.from_uci(move))

    def pprint_tree(self, node, _prefix="", _last=True):
        print(_prefix, "`- " if _last else "|- ", node.board.fen(), sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, _prefix, _last)
