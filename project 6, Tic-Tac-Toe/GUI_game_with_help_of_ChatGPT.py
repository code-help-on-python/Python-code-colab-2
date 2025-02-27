import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        # Ask the user for a difficulty level
        self.difficulty = simpledialog.askstring("Difficulty",
                                                 "Choose difficulty level: easy, medium, or hard",
                                                 parent=self.root)
        if self.difficulty is None or self.difficulty.lower() not in ['easy', 'medium', 'hard']:
            self.difficulty = 'easy'
        else:
            self.difficulty = self.difficulty.lower()

        # Initialize the game board and GUI components
        self.board = [" "] * 9
        self.buttons = []
        self.game_over = False
        self.create_board()

    def create_board(self):
        # Create a 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=('Helvetica', 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_button_click(self, index):
        # If game is over or the cell is not empty, do nothing
        if self.game_over or self.board[index] != " ":
            return

        # Human makes a move
        self.board[index] = "X"
        self.buttons[index].config(text="X")

        if self.check_win("X"):
            self.game_over = True
            messagebox.showinfo("Game Over", "Congratulations, you win!")
            self.ask_restart()
            return
        elif self.check_draw():
            self.game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
            self.ask_restart()
            return

        # Schedule the computer's move after a short delay
        self.root.after(500, self.ai_turn)

    def ai_turn(self):
        if self.game_over:
            return

        move = self.get_ai_move()
        if move is not None:
            self.board[move] = "O"
            self.buttons[move].config(text="O")

            if self.check_win("O"):
                self.game_over = True
                messagebox.showinfo("Game Over", "Computer wins! Better luck next time!")
                self.ask_restart()
                return
            elif self.check_draw():
                self.game_over = True
                messagebox.showinfo("Game Over", "It's a draw!")
                self.ask_restart()
                return

    def get_ai_move(self):
        # Choose the move based on selected difficulty
        if self.difficulty == "easy":
            return random.choice(self.available_moves())
        elif self.difficulty == "medium":
            # Try to win
            for move in self.available_moves():
                board_copy = self.board.copy()
                board_copy[move] = "O"
                if self.is_winner(board_copy, "O"):
                    return move
            # Block player's winning move
            for move in self.available_moves():
                board_copy = self.board.copy()
                board_copy[move] = "X"
                if self.is_winner(board_copy, "X"):
                    return move
            return random.choice(self.available_moves())
        elif self.difficulty == "hard":
            move, _ = self.minimax(self.board, True)
            return move
        return random.choice(self.available_moves())

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def check_win(self, player):
        return self.is_winner(self.board, player)

    def is_winner(self, board, player):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combos:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False

    def check_draw(self):
        return " " not in self.board

    def minimax(self, board, is_maximizing):
        # Terminal conditions
        if self.is_winner(board, "O"):
            return None, 1
        if self.is_winner(board, "X"):
            return None, -1
        if " " not in board:
            return None, 0

        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for move in [i for i, spot in enumerate(board) if spot == " "]:
                board[move] = "O"
                _, score = self.minimax(board, False)
                board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score
        else:
            best_score = float('inf')
            best_move = None
            for move in [i for i, spot in enumerate(board) if spot == " "]:
                board[move] = "X"
                _, score = self.minimax(board, True)
                board[move] = " "
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score

    def ask_restart(self):
        if messagebox.askyesno("Restart", "Would you like to play again?"):
            self.reset_game()
        else:
            self.root.quit()

    def reset_game(self):
        self.board = [" "] * 9
        for button in self.buttons:
            button.config(text=" ")
        self.game_over = False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
    