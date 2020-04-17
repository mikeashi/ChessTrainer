var board = null
var game = new Chess()


/**
 * returns the start position
 */
var getStartPosition = function () {
    // todo load starting position fen
    return 'start';
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
 * onDrop function
 */
var onDrop = function (source, target) {
    // see if the move is legal
    var move = game.move({
        from: source,
        to: target,
        promotion: 'q' // TODO fix this : always promote to a queen for example simplicity
    });

    // illegal move
    if (move === null) return 'snapback';

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
    console.log('updated')
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
    $status = $('#status')
    $fen = $('#fen')
    $pgn = $('#pgn')
    console.log($status)
    updateStatus();
};
