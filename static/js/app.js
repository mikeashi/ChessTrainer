/**
 * returns the start position
 */
var getStartPosition = function(){
    // todo load starting position fen
    return 'start';
}

/**
 * onDragStart function
 */
var onDragStart = function(source, piece, position, orientation) {
    // do not pick up pieces if the game is over
    // only pick up pieces for the side to move
  if (game.game_over() === true ||
      (game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
    return false;
  }
};
/**
 * onDrop function
 */
var onDrop = function(source, target) {
  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // TODO fix this : always promote to a queen for example simplicity
  });

  // illegal move
  if (move === null) return 'snapback';
};

/**
 * onSnapEnd function
 */
var onSnapEnd = function() {
    // update the board position after the piece snap
    // for castling, en passant, pawn promotion
    board.position(game.fen());
};

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
var init = function() {
    console.log(config);
    let board = new ChessBoard('board',config);
};
