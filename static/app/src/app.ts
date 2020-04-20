const $ = require("jquery");
const Chessground = require('chessground').Chessground;
const Chess = require('chess.js').Chess;
const chess = new Chess();

/**
 * return starting fen.
 */
function getStartPositionFen(): string {
    let fen = null;
    $.ajax({
        async: false,
        type: 'GET',
        url: "/get_start",
        success: function (data: string) {
            fen = data
        }
    });
    return fen;
}

/**
 * return moves.
 */
function getMoves(): string[] {
    let moves: string[] = []
    $.ajax({
        async: false,
        type: 'GET',
        url: "/get_moves",
        success: function (data: string) {
            moves = JSON.parse(data);
        }
    });
    return moves;
}

/**
 * return available moves
 */
function toDests() {
    const dest = {};
    // @ts-ignore
    getMoves().forEach(m => {
        // @ts-ignore
        dest[m[0]] = [m[1]];
    });
    return dest;
}

/**
 * return the player color
 * @param chess
 */
function toColor(chess: any) {
    return (chess.turn() === 'w') ? 'white' : 'black';
}

/**
 * register Move
 * @param move
 */
function registerMove(move:string) {
    console.log('registerd move: ' + move)
    $.get("/play/" + move)
}


// @ts-ignore
function playOtherSide(board, chess) {
    return (orig: any, dest: any) => {
        chess.move({from: orig, to: dest});
        board.set({
            turnColor: toColor(chess),
            movable: {
                color: toColor(chess),
                dests: toDests()
            }
        });
    };
}


const config = {
    fen: getStartPositionFen(),
    movable: {
        color: 'white',
        free: false,
        dests: toDests(),
    },
    draggable: {
        showGhost: true
    }
};

const board = Chessground(document.getElementById('chessboard'), config);

// @ts-ignore
window['board'] = board;


board.set({
    movable: {events: {after: playOtherSide(board, chess)}}
});
