import random
import math
import copy

class Board:
    ROWS = 6
    COLS = 7

    def __init__(self):
        self.board = [[' ' for i in range(self.COLS)] for i in range(self.ROWS)]
        self.history = []
        # Makes a board consiting of empty strings
        self.last_move = None
        self.valid_locations = []

    def can_play(self, col):
        # Checks that column is not full and in the range of the board
        return 0 <= col < self.COLS and self.board[0][col] == ' '

    def play(self, col, piece):
        # Plays a piece to the board
        if not self.can_play(col):
            raise ValueError("Column is full or out of bounds")
        row = self.get_next_open_row(col)
        self.board[row][col] = str(piece)
        self.last_move = (row, col)
        self.history.append((piece,col))

    def get_next_open_row(self, col):
        # Searches the playable row
        for r in range(self.ROWS - 1, -1, -1):
            if self.board[r][col] == ' ':
                return r
        return None

    def is_winning(self, piece):
        # Check horizontal
        for r in range(self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.board[r][c + i] == piece for i in range(4)):
                    return True

        # Check vertical
        for c in range(self.COLS):
            for r in range(self.ROWS - 3):
                if all(self.board[r + i][c] == piece for i in range(4)):
                    return True

        # Check positively sloped diagonals
        for r in range(self.ROWS - 3):
            for c in range(self.COLS - 3):
                if all(self.board[r + i][c + i] == piece for i in range(4)):
                    return True

        # Check negatively sloped diagonals
        for r in range(3, self.ROWS):
            for c in range(self.COLS - 3):
                if all(self.board[r - i][c + i] == piece for i in range(4)):
                    return True
        return False

    def print_board(self):
        # Returns the board as a string
        rows = ['|' + '|'.join(row) + '|' for row in self.board]
        board_str = "\n".join(rows)
        col_str = ' ' + ' '.join(str(i) for i in range(self.COLS))
        return board_str + "\n" + col_str

    def get_valid_locations(self):
        # Returns all playable columns
        valid_locations = []
        for col in range(self.COLS):
            if self.can_play(col):
                valid_locations.append(col)
        return valid_locations


def minimax(board, depth, alpha, beta, maximizing_player, piece):
    # Base cases for recursion
    is_terminal_node = board.is_winning('0') or board.is_winning('1') or len(board.get_valid_locations()) == 0

    if depth == 0 or is_terminal_node:
        if is_terminal_node:
            if board.is_winning(str(piece)): # Winning
                return (1000000, None)
            if board.is_winning('1' if piece == '0' else '0'): # Losing
                return (-1000000, None)
            return (0, None) # Draw
        return (eval_board(board, piece), None) # depth 0

    if maximizing_player:
        value = -math.inf
        best_col = random.choice(board.get_valid_locations()) # A random initial choice

        for col in board.get_valid_locations():
            temp_board = copy.deepcopy(board)
            temp_board.play(col, piece)
            new_score = minimax(temp_board, depth - 1, alpha, beta, False, piece)[0]

            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return (value, best_col)

    # Minimizing player
    value = math.inf
    best_col = random.choice(board.get_valid_locations())

    for col in board.get_valid_locations():
        temp_board = copy.deepcopy(board)
        temp_board.play(col, '1' if piece == '0' else '0')
        new_score = minimax(temp_board, depth - 1, alpha, beta, True, piece)[0]

        if new_score < value:
            value = new_score
            best_col = col
        beta = min(beta, value)
        if alpha >= beta:
            break
    return (value, best_col)

def eval_board(board, piece):
    # Heuristic function
    score = 0
    opponent_piece = '1' if piece == '0' else '0'

    # Score center column
    center_array = [row[board.COLS // 2] for row in board.board]
    center_count = center_array.count(str(piece))
    score += center_count * 3

    # Simple check for immediate win/loss
    if board.is_winning(str(piece)):
        return 1000000
    if board.is_winning(str(opponent_piece)):
        return -1000000

    return score

def player_loop():
    # loop for player
    command = input("press a row 0-6 to play the piece or press P to let the AI play")
    return command

def end_logic(board,piece):
    win = board.is_winning(str(piece))
    if win:
        print(board.print_board())
        print(f"Game over: {piece} won")
        return True
    return False

def change_turn(piece):
    if piece == 0:
        piece += 1
        return piece
    else:
        piece = 0
        return piece

def start_new():
    # Main loop
    board = Board()
    piece = 0
    board.print_board()
    move = None
    return board, piece, move


def main():
    board, piece, move = start_new()
    while True:
        # Read input commands from the program
        command = input().strip()

        if "PLAY" in command:
            move = minimax(board, 5, -math.inf, math.inf, True, piece)[1]
            board.play(move,piece)

        if "MOVE" in command:
            player_choice = int(command.replace("MOVE:",""))
            board.play(player_choice,piece)
            move = player_choice

        if "RESET" in command:
            main()

        if end_logic(board,piece):
            break

        piece = change_turn(piece)

        print(command)
        print(board.print_board())
        print(board.history)
if __name__ == "__main__":
    main()
