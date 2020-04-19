import json

import chess

from Core.tree import Tree


class App:

    def __init__(self):
        self.tree = Tree()

    def register_move_from_uci(self, uci):
        self.tree.register_move(chess.Move.from_uci(uci))

    def fen(self):
        return self.tree.current.board.fen()

    def status(self):
        return self.tree.to_json()

    def get_moves(self):
        return json.dumps(self.tree.get_moves())

    def get_turn(self):
        return self.tree.current.board.turn

    def load(self):
        self.tree.from_json('{"fen": "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1", "move": "", '
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
                            '"hash": 551671236195985012, "children": [{"fen": '
                            '"rnbqkb1r/ppp2ppp/4pn2/3p4/2PP4/2N5/PP2PPPP/R1BQKBNR w KQkq - 2 4", "move": "g8f6", '
                            '"hash": 6650087000524810210, "children": [{"fen": '
                            '"rnbqkb1r/ppp2ppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR b KQkq - 3 4", "move": "c1g5", '
                            '"hash": 11102373440004537386, "children": [{"fen": '
                            '"rnbqk2r/ppp1bppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR w KQkq - 4 5", "move": "f8e7", '
                            '"hash": 10295226814722216123, "children": [{"fen": '
                            '"rnbqk2r/ppp1bppp/4pn2/3P2B1/3P4/2N5/PP2PPPP/R2QKBNR b KQkq - 0 5", "move": "c4d5", '
                            '"hash": 9292445489617568934, "children": [{"fen": '
                            '"rnbqk2r/ppp1bppp/5n2/3p2B1/3P4/2N5/PP2PPPP/R2QKBNR w KQkq - 0 6", "move": "e6d5", '
                            '"hash": 13826539264373146733, "children": [{"fen": '
                            '"rnbqk2r/ppp1bppp/5n2/3p2B1/3P4/2N1P3/PP3PPP/R2QKBNR b KQkq - 0 6", "move": "e2e3", '
                            '"hash": 1354737440646778057, "children": [{"fen": '
                            '"r1bqk2r/ppp1bppp/2n2n2/3p2B1/3P4/2N1P3/PP3PPP/R2QKBNR w KQkq - 1 7", "move": "b8c6", '
                            '"hash": 13339985783667157450, "children": [{"fen": '
                            '"r1bqk2r/ppp1bppp/2n2n2/3p2B1/3P4/2NBP3/PP3PPP/R2QK1NR b KQkq - 2 7", "move": "f1d3", '
                            '"hash": 17018126378039323577, "children": [{"fen": '
                            '"r1bq1rk1/ppp1bppp/2n2n2/3p2B1/3P4/2NBP3/PP3PPP/R2QK1NR w KQ - 3 8", "move": "e8g8", '
                            '"hash": 16610518362247971410, "children": [{"fen": '
                            '"r1bq1rk1/ppp1bppp/2n2n2/3p2B1/3P4/2NBPN2/PP3PPP/R2QK2R b KQ - 4 8", "move": "g1f3", '
                            '"hash": 4458711549166658415, "children": [{"fen": '
                            '"r1bqr1k1/ppp1bppp/2n2n2/3p2B1/3P4/2NBPN2/PP3PPP/R2QK2R w KQ - 5 9", "move": "f8e8", '
                            '"hash": 2427794001084172013, "children": [{"fen": '
                            '"r1bqr1k1/ppp1bppp/2n2n2/3p2B1/3P4/2NBPN2/PP3PPP/R2Q1RK1 b - - 6 9", "move": "e1g1", '
                            '"hash": 6900705346847874557, "children": null}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}]}')
