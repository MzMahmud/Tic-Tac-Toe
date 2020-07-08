class State:
    SIZE = 3
    EMPTY = 0

    def __init__(self, board=None):
        if not board is None:
            self.board = [
                [board[i][j] for i in range(State.SIZE)] for j in range(State.SIZE)
            ]
        else:
            self.board = [
                [State.EMPTY for _ in range(State.SIZE)] for _ in range(State.SIZE)
            ]

    def get_legal_moves(self):
        return [
            (i, j)
            for i in range(State.SIZE)
            for j in range(State.SIZE)
            if self.board[i][j] == State.EMPTY
        ]

    def make_move(self, pos, marker):
        i, j = pos[0], pos[1]
        if self.board[i][j] == State.EMPTY:
            self.board[i][j] = marker
            return True
        return False

    def undo_move(self, pos):
        i, j = pos[0], pos[1]
        self.board[i][j] = State.EMPTY

    def result(self):
        board = self.board
        # row match
        for i in range(3):
            if self.board[i][0] == State.EMPTY:
                continue
            if self.board[i][0] == board[i][1] and board[i][0] == board[i][2]:
                return self.board[i][0]

        # col match
        for i in range(3):
            if board[0][i] == State.EMPTY:
                continue
            if board[0][i] == board[1][i] and board[0][i] == board[2][i]:
                return board[0][i]

        if (
            board[0][0] != State.EMPTY
            and board[0][0] == board[1][1]
            and board[0][0] == board[2][2]
        ):
            return board[0][0]

        if (
            board[0][2] != State.EMPTY
            and board[0][2] == board[1][1]
            and board[0][2] == board[2][0]
        ):
            return board[0][2]

        for i in range(3):
            for j in range(3):
                if board[i][j] == State.EMPTY:
                    return None
        return "draw"

    def __str__(self):
        return str(self.board)
