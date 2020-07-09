from state import State
from minimax import minimax


def show(state):
    for i in range(3):
        print(end="            ")
        for j in range(3):
            if state.board[i][j] != state.EMPTY:
                print(state.board[i][j], end=" ")
            else:
                print(" ", end=" ")
            if j != 2:
                print(end="| ")
        print()
        if i != 2:
            print("            ---------")
    print()


def make_move(state, key, turn):
    try:
        key = int(key)
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
        if key < 1 or key > 9:
            return False
        return state.make_move(pos[key], turn)
    except:
        return False
    


def filter_case(player):
    if player in {"0", "O", "o"}:
        return "O"
    if player in {"X", "x", "*"}:
        return "X"
    return player


def game_play(with_ai):
    player = filter_case(input("Choose your Marker (O or X) [X goes FIRST]: "))
    while not player in {"O", "X"}:
        print("\n****Invalid Choise!! TRY AGAIN****\n")
        player = filter_case(input("Choose your Marker (O or X) [X goes FIRST]: "))

    print("\n--------------Instruction---------------")
    print("***Use yout Number pad to choose cell***")
    print("             7 |  8  | 9")
    print("            -------------")
    print("             4 |  5  | 6")
    print("            -------------")
    print("             1 |  2  | 3")
    print("********Press ENTER to Give Move********\n\n\n")

    state = State()
    turn = "X"
    result = None
    while result is None:
        print(f"----{turn}'s MOVE----'")
        if turn == player:
            key = input("Make Move using Number Pad 1 to 9: ")
            if not make_move(state, key, turn):
                print("Invalid input! Try Again")
                continue
        else:
            if with_ai:
                print("----Its AI's Turn!----")
                print("....Thinking.....")
                ai_move = minimax(state, turn)[1]
                state.make_move(ai_move, turn)
                print("---AI made a move. Your turn!---")
            else:
                key = input("Make Move using Number Pad 1 to 9: ")
                if not make_move(state, key, turn):
                    print("Invalid input! Try Again")
                    continue
        show(state)
        turn = "O" if turn == "X" else "X"
        result = state.result()

    if result == "draw":
        print(f"----DRAW!!----")
    else:
        print(f"----{result} WON!!----")
    if with_ai:
        if result == player:
            print("****CONGRATS!!****")
            print("You WON against COMPUTER!!")
        elif result == "draw":
            print("Good Jod!! You have DRAWN with computer!")
        else:
            print("----Computer WON!!----")

    print("\n1.  Play AGAIN")
    print("0.  Main Menue")
    print("00. EXIT\n")
    choise = input("Enter your choise: ")
    while not choise in {"1", "0", "00"}:
        print("***Invalid Input. TRY again***\n")
        choise = input("Enter your choise: ")
    
    if choise in {"0","00"}:
        return choise
    return choise if with_ai else "2"


running = True
while running:
    print("-----Welcome To Number Pad Tic-Tac-Toe----")
    print("1. Play With Computer")
    print("2. Two Player")
    print("0. Quit\n")

    choise = input("Enter your choise: ")
    while not choise in {"1", "2", "0"}:
        print("***Invalid Input. TRY again***\n")
        choise = input("Enter your choise: ")

    if choise in {"0", "O", "o"}:
        quit()
    
    while choise in {"1","2"}:
        choise = game_play(choise == "1")
        if choise == "00":
            running = False

