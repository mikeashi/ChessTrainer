import chess.polyglot


class BoardHelper:

    @staticmethod
    def hash(board: chess.Board):
        return chess.polyglot.zobrist_hash(board)

    @staticmethod
    def get_pseudo_board(board: chess.Board, move: chess.Move):
        pseudo_board = board.__copy__()
        pseudo_board.push(move)
        return pseudo_board
