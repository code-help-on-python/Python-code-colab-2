import random

class TicTacToe:
    def __init__(self):
        self.cells = [' ' for _ in range(9)]

    def print_board(self):
        print("---------")
        for i in range(0, 9, 3):
            print('--+--+--')
            print(f"| {self.cells[i]} {self.cells[i+1]} {self.cells[i+2]} |")
        print("---------")

    def check_winner(self, mark):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for condition in win_conditions:
            if all(self.cells[i] == mark for i in condition):
                return True
        return False

game = TicTacToe()
game.print_board()
