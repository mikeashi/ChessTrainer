from Core.tree import Tree
import chess

tree = Tree()

def print_path(node):
    stack = [node]
    while True:
        tmp = stack.pop()
        print(tmp.move)
        child_count = len(tmp.children)
        if child_count > 1:
            for child in tmp.children:
                print('(')
                print_path(child)
                print(')')
        elif child_count == 1:
            stack.append(tmp.children[0])
        if len(stack) == 0:
            break


# first line
tree.register_move(chess.Move.from_uci('d2d4'))
tree.register_move(chess.Move.from_uci('d7d5'))
tree.register_move(chess.Move.from_uci('c2c4'))
tree.register_move(chess.Move.from_uci('e7e6'))
tree.register_move(chess.Move.from_uci('b1c3'))
tree.register_move(chess.Move.from_uci('g8f6'))
tree.register_move(chess.Move.from_uci('c4d5'))
tree.register_move(chess.Move.from_uci('e6d5'))
tree.register_move(chess.Move.from_uci('c1g5'))
tree.register_move(chess.Move.from_uci('f8e7'))
tree.register_move(chess.Move.from_uci('e2e3'))
tree.register_move(chess.Move.from_uci('c7c6'))
tree.register_move(chess.Move.from_uci('f1d3'))
tree.register_move(chess.Move.from_uci('b8d7'))
tree.register_move(chess.Move.from_uci('d1c2'))
tree.register_move(chess.Move.from_uci('e8g8'))
tree.register_move(chess.Move.from_uci('g1f3'))
tree.register_move(chess.Move.from_uci('f8e8'))
tree.register_move(chess.Move.from_uci('e1g1'))
tree.back_to_root()

# second line
tree.register_move(chess.Move.from_uci('d2d4'))
tree.register_move(chess.Move.from_uci('d7d5'))
tree.register_move(chess.Move.from_uci('c2c4'))
tree.register_move(chess.Move.from_uci('e7e6'))
tree.register_move(chess.Move.from_uci('b1c3'))
tree.register_move(chess.Move.from_uci('c7c6'))
tree.register_move(chess.Move.from_uci('e2e3'))
tree.register_move(chess.Move.from_uci('g8f6'))
tree.register_move(chess.Move.from_uci('g1f3'))
tree.register_move(chess.Move.from_uci('b8d7'))
tree.register_move(chess.Move.from_uci('d1c2'))
tree.register_move(chess.Move.from_uci('f8d6'))
tree.register_move(chess.Move.from_uci('f1d3'))
tree.register_move(chess.Move.from_uci('e8g8'))
tree.register_move(chess.Move.from_uci('e1g1'))
tree.register_move(chess.Move.from_uci('d5c4'))
tree.register_move(chess.Move.from_uci('d3c4'))
tree.register_move(chess.Move.from_uci('b7b5'))
tree.register_move(chess.Move.from_uci('c4e2'))
tree.back_to_root()

# 3. line

tree.register_move(chess.Move.from_uci('d2d4'))
tree.register_move(chess.Move.from_uci('d7d5'))
tree.register_move(chess.Move.from_uci('c2c4'))
tree.register_move(chess.Move.from_uci('e7e6'))
tree.register_move(chess.Move.from_uci('b1c3'))
tree.register_move(chess.Move.from_uci('f8e7'))
tree.register_move(chess.Move.from_uci('g1f3'))
tree.register_move(chess.Move.from_uci('g8f6'))
tree.register_move(chess.Move.from_uci('c1g5'))
tree.register_move(chess.Move.from_uci('h7h6'))
tree.register_move(chess.Move.from_uci('g5h4'))
tree.register_move(chess.Move.from_uci('e8g8'))
tree.register_move(chess.Move.from_uci('e2e3'))
tree.register_move(chess.Move.from_uci('b7b6'))
tree.register_move(chess.Move.from_uci('f1d3'))
tree.register_move(chess.Move.from_uci('c8b7'))
tree.register_move(chess.Move.from_uci('e1g1'))
tree.register_move(chess.Move.from_uci('b8d7'))
tree.register_move(chess.Move.from_uci('d1e2'))
tree.back_to_root()

print_path(tree.root)
