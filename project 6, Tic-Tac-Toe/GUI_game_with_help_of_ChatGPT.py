import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Create a control panel for the dropdown and New Game button.
        control_frame = tk.Frame(self.root)
        control_frame.pack(side=tk.TOP, pady=10)
        
        tk.Label(control_frame, text="Select Difficulty:").pack(side=tk.LEFT, padx=5)
        # Use a StringVar to hold the difficulty setting.
        self.difficulty_var = tk.StringVar(value="easy")
        difficulty_menu = tk.OptionMenu(control_frame, self.difficulty_var, "easy", "medium", "hard")
        difficulty_menu.pack(side=tk.LEFT, padx=5)
        
        new_game_button = tk.Button(control_frame, text="New Game", command=self.reset_game)
        new_game_button.pack(side=tk.LEFT, padx=5)
        
        # Create the frame for the Tic Tac Toe board.
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack()
        
        # Initialize game state.
        self.board = [" "] * 9
        self.buttons = []
        self.game_over = False
        self.create_board()
        
        # Set players: human is always "X", computer is "O".
        self.human = "X"
        self.computer = "O"
        self.current_player = self.human  # Human starts first

    def create_board(self):
        # Clear any existing buttons (helpful when resetting the game).
        for widget in self.board_frame.winfo_children():
            widget.destroy()
        self.buttons = []
        
        # Create a 3x3 grid of buttons.
        for i in range(9):
            button = tk.Button(self.board_frame, text=" ", font=('Helvetica', 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    
    def on_button_click(self, index):
        if self.game_over or self.board[index] != " ":
            return
        
        # Human makes a move.
        self.board[index] = self.human
        self.buttons[index].config(text=self.human)
        self.root.update_idletasks()  # Force the board to update
        
        if self.check_win(self.human):
            self.game_over = True
            # Delay showing the win message so the move is visible.
            self.root.after(500, lambda: self.end_game("Congratulations, you win!"))
            return
        elif self.check_draw():
            self.game_over = True
            self.root.after(500, lambda: self.end_game("It's a draw!"))
            return
        
        # Switch to the computer's turn after a short delay.
        self.current_player = self.computer
        self.root.after(500, self.ai_turn)
    
    def ai_turn(self):
        if self.game_over:
            return
        
        # Use the current difficulty setting from the dropdown.
        difficulty = self.difficulty_var.get()
        move = self.get_ai_move(difficulty)
        if move is not None:
            self.board[move] = self.computer
            self.buttons[move].config(text=self.computer)
            self.root.update_idletasks()  # Update the board so the move shows
            
            if self.check_win(self.computer):
                self.game_over = True
                self.root.after(500, lambda: self.end_game("Computer wins! Better luck next time!"))
                return
            elif self.check_draw():
                self.game_over = True
                self.root.after(500, lambda: self.end_game("It's a draw!"))
                return
        
        # Switch back to the human's turn.
        self.current_player = self.human
    
    def get_ai_move(self, difficulty):
        if difficulty == "easy":
            # Random move—sometimes a little unpredictability is fun!
            return random.choice(self.available_moves())
        elif difficulty == "medium":
            # First, try to win.
            for move in self.available_moves():
                board_copy = self.board.copy()
                board_copy[move] = self.computer
                if self.is_winner(board_copy, self.computer):
                    return move
            # Then block the human's winning move.
            for move in self.available_moves():
                board_copy = self.board.copy()
                board_copy[move] = self.human
                if self.is_winner(board_copy, self.human):
                    return move
            # Otherwise, pick randomly.
            return random.choice(self.available_moves())
        elif difficulty == "hard":
            # Use the minimax algorithm for an optimal move.
            move, _ = self.minimax(self.board, True)
            return move
        return random.choice(self.available_moves())
    
    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def check_win(self, player):
        return self.is_winner(self.board, player)
    
    def is_winner(self, board, player):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for combo in winning_combos:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
                return True
        return False
    
    def check_draw(self):
        return " " not in self.board
    
    def minimax(self, board, is_maximizing):
        if self.is_winner(board, self.computer):
            return None, 1
        if self.is_winner(board, self.human):
            return None, -1
        if " " not in board:
            return None, 0
        
        if is_maximizing:
            best_score = -float('inf')
            best_move = None
            for move in self.available_moves():
                board[move] = self.computer
                _, score = self.minimax(board, False)
                board[move] = " "
                if score > best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score
        else:
            best_score = float('inf')
            best_move = None
            for move in self.available_moves():
                board[move] = self.human
                _, score = self.minimax(board, True)
                board[move] = " "
                if score < best_score:
                    best_score = score
                    best_move = move
            return best_move, best_score
    
    def end_game(self, message):
        messagebox.showinfo("Game Over", message)
        self.ask_restart()
    
    def ask_restart(self):
        if messagebox.askyesno("Restart", "Would you like to play again?"):
            self.reset_game()
        else:
            self.root.quit()
    
    def reset_game(self):
        # Reset the board and game state without restarting the application.
        self.board = [" "] * 9
        self.game_over = False
        self.current_player = self.human
        for button in self.buttons:
            button.config(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()
