from state import State
from random import shuffle


MIN_PLAYER = "O"
MAX_PLAYER = "X"
score = {MIN_PLAYER: -1, MAX_PLAYER: 1, "draw": 0}


def minimax(current_state, player):
    result = current_state.result()
    if not (result is None):
        return (score[result], None)

    moves = current_state.get_legal_moves()
    shuffle(moves)
    if player == MAX_PLAYER:
        max_val, opt_move = None, None
        for move in moves:
            current_state.make_move(move, MAX_PLAYER)
            val = minimax(current_state, MIN_PLAYER)[0]
            if (max_val is None) or (val > max_val):
                max_val = val
                opt_move = move
            current_state.undo_move(move)
        return (max_val, opt_move)
    elif player == MIN_PLAYER:
        min_val, opt_move = None, None
        for move in moves:
            current_state.make_move(move, MIN_PLAYER)
            val = minimax(current_state, MAX_PLAYER)[0]
            if (min_val is None) or (val < min_val):
                min_val = val
                opt_move = move
            current_state.undo_move(move)
        return (min_val, opt_move)

