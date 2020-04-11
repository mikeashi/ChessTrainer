from unittest import TestCase
from app import App
import chess


class TestApp(TestCase):

    def test_it_starts_from_the_starting_position(self):
        app = App.start()
        self.assertEqual(app.board.board_fen(), chess.STARTING_BOARD_FEN)

    def test_it_starts_from_the_given_position(self):
        app = App.start_from_position("rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 2 4")
        self.assertEqual(app.board.board_fen(), "rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR")