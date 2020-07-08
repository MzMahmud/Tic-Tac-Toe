from state import State
from minimax import minimax


def show(state):
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != state.EMPTY:
                print(state.board[i][j], end=" ")
            else:
                print(" ", end=" ")
            if j != 2:
                print(end="| ")
        print()
        if i != 2:
            print("---------")
    print()


def make_move(state, key, turn):
    pos = {
        7: (0, 0),
        8: (0, 1),
        9: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        1: (2, 0),
        2: (2, 1),
        3: (2, 2),
    }
    return state.make_move(pos[key], turn)


state = State()
turn = "O"
result = None
while result is None:
    print(f"---{turn}'s MOVE---'")
    if turn == "O":
        print("---Its AI's Turn!---")
        print("...Thinking....")
        ai_move = minimax(state, turn)[1]
        state.make_move(ai_move, turn)
        print("---AI made a move. Your turn!---")
    else:
        key = int(input("Make Move number in range [1,9]: "))
        if not make_move(state, key, turn):
            print("Invalid input! Try Again")
            continue

    show(state)
    turn = "O" if turn == "X" else "X"
    result = state.result()

# print(result)
if result == "draw":
    print("Drawn!")
else:
    print(f"---{result} WON!!---")
