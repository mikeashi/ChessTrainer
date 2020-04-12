from unittest import TestCase

import chess

from Core.tree import Tree


class TestTree(TestCase):
    def setUp(self):
        self.tree = Tree.from_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        pass

    def test_register_a_new_move(self):
        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.tree.reset_current()
        self.tree.register_move(chess.Move.from_uci('d2d4'))
        self.assertEqual(2, len(self.tree.root.children))

    def test_register_does_not_create_a_new_node_when_the_given_move_is_already_part_of_the_tree(self):
        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.tree.reset_current()
        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.assertEqual(1, len(self.tree.root.children))

    def test_it_keeps_track_of_all_lines(self):
        self.tree.register_move(chess.Move.from_uci('d2d4'))
        self.tree.register_move(chess.Move.from_uci('d7d5'))
        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.tree.register_move(chess.Move.from_uci('e7e5'))
        self.tree.reset_current()

        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.tree.register_move(chess.Move.from_uci('e7e5'))
        self.tree.register_move(chess.Move.from_uci('d2d4'))
        self.tree.register_move(chess.Move.from_uci('d7d5'))
        self.tree.reset_current()

        self.tree.register_move(chess.Move.from_uci('d2d4'))
        self.tree.register_move(chess.Move.from_uci('e7e5'))
        self.tree.register_move(chess.Move.from_uci('e2e4'))
        self.tree.register_move(chess.Move.from_uci('d7d5'))
        self.tree.reset_current()

        # root has two lines: the first starts with d4 and the other e4
        self.assertEqual(2, len(self.tree.root.children))
        # after d4 there is two lines: d5 and e5
        self.assertEqual(2, len(self.tree.root.children[0].children))
        # after e4 there is one line: e5
        self.assertEqual(1, len(self.tree.root.children[1].children))
