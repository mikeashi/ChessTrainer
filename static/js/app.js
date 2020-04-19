var board = null
var game = null


/**
 * returns the start position
 */
var getStartPosition = function () {
    var fen = 'start'

    $.ajax({
        async: false,
        type: 'GET',
        url: "/get_start",
        success: function (data) {
             fen = data
        }
    });

    return fen;
}

/**
 * onDragStart function
 */
var onDragStart = function (source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    if (game.game_over()) return false

    // only pick up pieces for the side to move
    if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
        (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
        return false
    }
};

/**
 * convert move from san to uci.
 *
 * @param move
 */
function SAN_to_UCI(move) {
    return move.from + move.to
}

/**
 * register Move
 * @param move
 */
function registerMove(move) {
    $.get("/play/" + SAN_to_UCI(move))
}

/**
 * onDrop function
 */
var onDrop = function (source, target) {
    moves = []

    $.ajax({
        async: false,
        type: 'GET',
        url: "/get_moves",
        success: function (data) {
            moves = JSON.parse(data);
        }
    });

    console.log(moves)
    console.log('move' + source+target)
    console.log('res:'+!moves.includes(source+target))

    // move not suggested
    if (!moves.includes(source+target)) return 'snapback';

    // see if the move is legal
    var move = game.move({
        from: source,
        to: target,
        promotion: 'q' // TODO fix this : always promote to a queen for example simplicity
    });

    // illegal move
    if (move === null) return 'snapback';

    registerMove(move)
    updateStatus();
};

/**
 * onSnapEnd function
 */
var onSnapEnd = function () {
    // update the board position after the piece snap
    // for castling, en passant, pawn promotion
    board.position(game.fen());
};

function updateStatus() {
    var status = ''

    var moveColor = 'White'
    if (game.turn() === 'b') {
        moveColor = 'Black'
    }

    // checkmate?
    if (game.in_checkmate()) {
        status = 'Game over, ' + moveColor + ' is in checkmate.'
    }

    // draw?
    else if (game.in_draw()) {
        status = 'Game over, drawn position'
    }

    // game still on
    else {
        status = moveColor + ' to move'

        // check?
        if (game.in_check()) {
            status += ', ' + moveColor + ' is in check'
        }
    }

    $status.html(status)
    $fen.html(game.fen())
    $pgn.html(game.pgn())
}

var config = {
    draggable: true,
    pieceTheme: 'static/img/cburnett/{piece}.svg',
    position: getStartPosition(),
    onDragStart: onDragStart,
    onDrop: onDrop,
    onSnapEnd: onSnapEnd
};

/**
 * init chess board
 */
var init = function () {
    board = new ChessBoard('board', config);
    game = new Chess(getStartPosition())
    $status = $('#status')
    $fen = $('#fen')
    $pgn = $('#pgn')
    updateStatus();
};


// did this based on a stackoverflow answer
// http://stackoverflow.com/questions/29493624/cant-display-board-whereas-the-id-is-same-when-i-use-chessboard-js
setTimeout(function () {
    init()
}, 0);
