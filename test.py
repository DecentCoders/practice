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

# Check if a player has won
print_board(init_board())
