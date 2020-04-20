const $ = require( "jquery" );
const Chessground = require('chessground').Chessground;
const Chess = require('chess.js').Chess;
const chess = new Chess();

/**
 * return starting fen.
 */
function getStartPositionFen():string {
    let fen = null;

    $.ajax({
        async: false,
        type: 'GET',
        url: "/get_start",
        success: function (data:string) {
             fen = data
        }
    });

    console.log('fen:' + fen);

    return fen;
}
/**
 * return available moves
 * @param chess
 */
function toDests(chess: any) {
    console.log('all the moves are comming from here !!')
    const dests = {};
    // @ts-ignore
    chess.SQUARES.forEach(s => {
        const ms = chess.moves({square: s, verbose: true});
        if (ms.length) {
            // @ts-ignore
            dests[s] = ms.map(m => m.to);
        }
    });
    console.log('moves:');
    console.log(dests);
    return dests;
}

/**
 * return the player color
 * @param chess
 */
function toColor(chess: any) {
    return (chess.turn() === 'w') ? 'white' : 'black';
}


// @ts-ignore
function playOtherSide(board, chess) {
    return (orig: any, dest: any) => {
        chess.move({from: orig, to: dest});
        board.set({
            turnColor: toColor(chess),
            movable: {
                color: toColor(chess),
                dests: toDests(chess)
            }
        });
    };
}


const config = {
    fen: getStartPositionFen(),
    movable: {
        color: 'white',
        free: false,
        dests: toDests(chess),
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
