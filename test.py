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

def check_draw(board):
    return " " not in board

# Get valid move from player
def get_valid_move(board, player):
    while True:
        move = input(f"Player {player}, enter your move (0-8): ")
        # Check if input is a number
        if not move.isdigit():
            print("Error! Enter a number between 0 and 8.")
            continue
        move = int(move)
        # Check if position is in 0-8 and empty
        if 0 <= move <= 8 and board[move] == " ":
            return move
        else:
            print("Invalid move! Position is taken or out of range. Try again.")

# Main game loop
def play_tic_tac_toe():
    print("=== Tic Tac Toe Game ===")
    print("Board Positions:")
    print(" 0 | 1 | 2 \n---+---+---\n 3 | 4 | 5 \n---+---+---\n 6 | 7 | 8 ")
    board = init_board()
    current_player = "X"  # X goes first

    while True:
        print_board(board)
        move = get_valid_move(board, current_player)
        board[move] = current_player  # Place the player's piece

        # Check if current player wins
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} WINS! 🎉")
            break
        # Check if it's a draw
        if check_draw(board):
            print_board(board)
            print("🤝 It's a DRAW! 🤝")
            break
        # Switch player (X ↔ O)
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_tic_tac_toe()