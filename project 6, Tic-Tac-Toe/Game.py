import random

class TicTacToe:
    def __init__(self):
        self.cells = ['' for _ in range(9)]
        self.player_sym = "X"       # Human's symbol
        self.computer_sym = "O"     # Computer's symbol
        self.medium_accuracy = 0.5  # Default accuracy for medium mode (adjustable from 0.0 to 1.0)

    def print_board(self):
        print("---------")
        for i in range(0, 9, 3):
            print("--+--+--")
            row = f"| {self.cells[i] or ' '} {self.cells[i+1] or ' '} {self.cells[i+2] or ' '} |"
            print(row)
        print("---------")

    def check_winner(self, mark):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if all(self.cells[i] == mark for i in condition):
                return True
        return False

    def easy(self):
        """Return a random available move index for easy difficulty."""
        moves = [i for i, cell in enumerate(self.cells) if cell == '']
        if moves:
            return random.choice(moves)
        return None

    def available_moves_board(self, board):
        """Return a list of indices for all empty cells in the board."""
        return [i for i, cell in enumerate(board) if cell == '']

    def is_winner_board(self, board, mark):
        """Check if the given mark ('X' or 'O') has won on the provided board."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for condition in win_conditions:
            if all(board[i] == mark for i in condition):
                return True
        return False

    def minimax(self, board, is_maximizing):
        """
The minimax function for Tic-Tac-Toe.

Parameters:
board (list): A list representing the board state (with "" for empty cells).
is_maximizing (bool): True if the current move is for the computer (maximizing),
False if for the human (minimizing).

Returns:
A tuple (best_move, score) where best_move is the index of the best move and
score is the evaluation of that move.
        """
        # Terminal conditions
        if self.is_winner_board(board, self.computer_sym):
            return None, 1   # Computer wins
        if self.is_winner_board(board, self.player_sym):
            return None, -1  # Human wins
        if not any(cell == "" for cell in board):
            return None, 0   # Draw

        if is_maximizing:
            best_score = -float("inf")
            best_move = None
            for move in self.available_moves_board(board):
                board[move] = self.computer_sym
                _, score = self.minimax(board, False)
                board[move] = ""
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score
        else:
            best_score = float("inf")
            best_move = None
            for move in self.available_moves_board(board):
                board[move] = self.player_sym
                _, score = self.minimax(board, True)
                board[move] = ""
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score

    def medium_move(self):
        """
Medium difficulty move with adjustable accuracy.
First, check for an immediate winning move for the computer.
Then check for a blocking move if the human is about to win.
Otherwise, with probability equal to medium_accuracy, use minimax;
else, pick a random move.
        """
        # Check immediate win for computer
        for move in self.available_moves_board(self.cells):
            self.cells[move] = self.computer_sym
            if self.check_winner(self.computer_sym):
                self.cells[move] = ""
                return move
            self.cells[move] = ""
        # Check immediate block for human
        for move in self.available_moves_board(self.cells):
            self.cells[move] = self.player_sym
            if self.check_winner(self.player_sym):
                self.cells[move] = ""
                return move
            self.cells[move] = ""

        # Otherwise, use minimax with probability medium_accuracy
        if random.random() < self.medium_accuracy:
            move, _ = self.minimax(self.cells.copy(), True)
            if move is not None:
                return move
        # Else choose a random move
        return random.choice(self.available_moves_board(self.cells))

    def play(self, difficulty="hard"):
        """
Run the main game loop.

Parameters:
difficulty (str): "easy", "medium", or "hard" mode for the computer.
        """
        current_turn = "human"  # Human always goes first
        while True:
            self.print_board()
            if current_turn == "human":
                try:
                    move = int(input("Enter your move (1-9): ")) - 1
                    if move < 0 or move > 8 or self.cells[move] != "":
                        print("Invalid move. Try again.")
                        continue
                    self.cells[move] = self.player_sym
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                if self.check_winner(self.player_sym):
                    self.print_board()
                    print("Congratulations, you win!")
                    break
                current_turn = "computer"
            else:
                print("Computer's turn...")
                if difficulty == "easy":
                    move = self.easy()
                elif difficulty == "medium":
                    move = self.medium_move()
                else:  # Hard mode uses minimax
                    move, _ = self.minimax(self.cells.copy(), True)
                if move is not None:
                    self.cells[move] = self.computer_sym
                    if self.check_winner(self.computer_sym):
                        self.print_board()
                        print("Computer wins! Better luck next time.")
                        break
                current_turn = "human"

            if all(cell != "" for cell in self.cells):
                self.print_board()
                print("It's a draw!")
                break

if __name__ == "__main__":
    print('''
---------
| 1 2 3 |
--+--+--
| 4 5 6 |
--+--+--
| 7 8 9 |
--------
    ''')
    game = TicTacToe()
    while True:
        difficulty = input("Choose computer difficulty (easy/medium/hard) exit to exit: ").strip().lower()
        if difficulty == 'exit':
            print("Bye, Had a nice game! Hope to see you soon.")
            break
        game.__init__()
        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = "hard"
        if difficulty == "medium":
            try:
                acc = float(input("Enter medium accuracy (0.0 to 1.0, where 1.0 is optimal): "))
                if 0.0 <= acc <= 1.0:
                    game.medium_accuracy = acc
                else:
                    print("Invalid value. Using default (0.5).")
            except ValueError:
                print("Invalid input. Using default (0.5).")
        game.play(difficulty)
