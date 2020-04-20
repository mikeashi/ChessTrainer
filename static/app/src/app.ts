const Chessground = require('chessground').Chessground;
const Chess = require('chess.js').Chess;


const chess = new Chess();

function setZoom(zoom: number) {
    const el = document.querySelector('.cg-wrap') as HTMLElement;
    if (el) {
        const px = `${zoom / 100 * 320}px`;
        el.style.width = px;
        el.style.height = px;
        document.body.dispatchEvent(new Event('chessground.resize'));
    }
}

function toDests(chess: any) {
    const dests = {};
    // @ts-ignore
    chess.SQUARES.forEach(s => {
        const ms = chess.moves({square: s, verbose: true});
        if (ms.length) {
            // @ts-ignore
            dests[s] = ms.map(m => m.to);
        }
    });
    return dests;
}


const config = {
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

//setZoom(200);
