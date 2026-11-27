def check_winner(board):
    # Define winning combinations by indices
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for a, b, c in wins:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board):
    return all(cell is not None for cell in board)

def simulate_game(board, turn):
    winner = check_winner(board)
    if winner is not None:
        # Game ended with a winner, count as one valid game
        print(board)
        return 1
    if is_full(board):
        # Board full without a winner -> draw, valid terminal game
        print(board)
        return 1

    valid_games = 0
    # Iterate over each empty cell and simulate a move
    for i in range(len(board)):
        if board[i] is None:
            # Create a new board state with the move applied
            new_board = board.copy()
            new_board[i] = turn

            # Check if the move immediately wins the game
            if check_winner(new_board) is not None or is_full(new_board):
                # This branch is terminal
                print(board)
                valid_games += 1
            else:
                # Otherwise, switch turn and keep playing
                next_turn = 'O' if turn == 'X' else 'X'
                valid_games += simulate_game(new_board, next_turn)
    return valid_games

# Initial empty board (9 cells)
initial_board = [None] * 9

# Start the simulation with 'X' since X always goes first.
total_valid_games = simulate_game(initial_board, 'X')
print("Total number of valid Tic Tac Toe games:", total_valid_games)
