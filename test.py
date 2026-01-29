# Initialize the game board (0-8 correspond to 3x3 grid positions)
def init_board():
    return [" " for _ in range(9)]

# Print the Tic Tac Toe board (formatted 3x3)
def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}  ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}  ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}  ")
    print("\n")

def check_win(board, player):
    # All winning combinations (3 in a row/column/diagonal)
    win_combinations = [
        [0,1,2], [3,4,5], [6,7,8],  # Horizontal
        [0,3,6], [1,4,7], [2,5,8],  # Vertical
        [0,4,8], [2,4,6]             # Diagonal
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Check if the board is full (draw)

