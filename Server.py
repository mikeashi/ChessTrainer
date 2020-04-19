from flask import Flask, render_template

from app import App

server = Flask(__name__)
app = App()
app.load()


@server.route('/')
def index():
    return render_template("index.html")


@server.route('/play/<path:move>')
def play_move(move):
    app.register_move_from_uci(move)
    return 'ok'


@server.route('/get_start')
def get_start():
    return app.fen()


@server.route('/get_turn')
def get_turn():
    return app.get_turn()

@server.route('/get_moves')
def get_moves():
    return app.get_moves()


@server.route('/status')
def status():
    return app.status()


def main():
    server.run()


if __name__ == '__main__':
    main()
