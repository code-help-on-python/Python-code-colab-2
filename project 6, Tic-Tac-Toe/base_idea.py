import random

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def check_draw(board):
    return " " not in board

def human_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Invalid move. Please choose a number between 1 and 9.")
            elif board[move] != " ":
                print("That space is already taken. Choose another!")
            else:
                return move
        except ValueError:
            print("Oops, please enter a valid number.")

def available_moves(board):
    return [i for i, spot in enumerate(board) if spot == " "]

def ai_move(board, difficulty, computer, human):
    if difficulty == "easy":
        # Easy mode: Random move (as unpredictable as a cat on a hot tin roof!)
        move = random.choice(available_moves(board))
        print("Computer (Easy) picks a random move!")
        return move
    elif difficulty == "medium":
        # Medium mode: Check if it can win or block you before taking a random move.
        # First, see if the computer can win on the next move.
        for move in available_moves(board):
            board_copy = board.copy()
            board_copy[move] = computer
            if check_win(board_copy, computer):
                print("Computer (Medium) spots a winning move!")
                return move
        # Next, block the human's winning move.
        for move in available_moves(board):
            board_copy = board.copy()
            board_copy[move] = human
            if check_win(board_copy, human):
                print("Computer (Medium) blocks your winning move!")
                return move
        # Otherwise, pick a random move.
        move = random.choice(available_moves(board))
        print("Computer (Medium) takes a random move!")
        return move
    elif difficulty == "hard":
        # Hard mode: Use the minimax algorithm to choose the best move.
        print("Computer (Hard) is calculating the optimal move...")
        move, _ = minimax(board, True, computer, human)
        return move
    else:
        # Default fallback.
        return random.choice(available_moves(board))

def minimax(board, is_maximizing, computer, human):
    # Check for terminal states.
    if check_win(board, computer):
        return None, 1
    elif check_win(board, human):
        return None, -1
    elif check_draw(board):
        return None, 0

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for move in available_moves(board):
            board[move] = computer
            _, score = minimax(board, False, computer, human)
            board[move] = " "
            if score > best_score:
                best_score = score
                best_move = move
        return best_move, best_score
    else:
        best_score = float('inf')
        best_move = None
        for move in available_moves(board):
            board[move] = human
            _, score = minimax(board, True, computer, human)
            board[move] = " "
            if score < best_score:
                best_score = score
                best_move = move
        return best_move, best_score

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("Choose difficulty level: easy, medium, or hard")
    difficulty = input("Enter difficulty: ").lower().strip()
    while difficulty not in ["easy", "medium", "hard"]:
        print("Invalid choice! Please choose from: easy, medium, or hard.")
        difficulty = input("Enter difficulty: ").lower().strip()

    board = [" "] * 9
    human = "X"
    computer = "O"
    current_player = human  # Human always starts first

    while True:
        print_board(board)
        if current_player == human:
            move = human_move(board)
            board[move] = human
            if check_win(board, human):
                print_board(board)
                print("Congratulations, you win!")
                break
            current_player = computer
        else:
            move = ai_move(board, difficulty, computer, human)
            board[move] = computer
            if check_win(board, computer):
                print_board(board)
                print("The computer wins! Better luck next time!")
                break
            current_player = human

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
    