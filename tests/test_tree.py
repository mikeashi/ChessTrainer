from unittest import TestCase

import chess

from Core.tree import Tree


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
        self.tree.back()
        self.register_move('d2d4')
        self.assertEqual(2, len(self.tree.root.children))

    def test_register_does_not_create_a_new_variation_when_the_given_move_is_already_part_of_the_tree(self):
        self.register_move('e2e4')
        self.tree.back()
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

    def register_move(self, move):
        self.tree.register_move(chess.Move.from_uci(move))

    def pprint_tree(self, node, _prefix="", _last=True):
        print(_prefix, "`- " if _last else "|- ", node.board.fen(), sep="")
        _prefix += "   " if _last else "|  "
        child_count = len(node.children)
        for i, child in enumerate(node.children):
            _last = i == (child_count - 1)
            self.pprint_tree(child, _prefix, _last)
