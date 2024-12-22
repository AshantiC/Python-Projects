import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    """
    Function to print the Tic-Tac-Toe board.
    The board is a list of 9 elements representing a 3x3 grid.
    """
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check if there's a winner
def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]  # diagonals
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

# Function for computer's move (chooses a random empty spot)
def computer_move(board):
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(empty_spots)
    board[move] = 'O'
    print(f"Computer chooses position {move + 1}\n")
    print_board(board)

# Function for player's move
def player_move(board):
    while True:
        try:
            move = int(input("Enter a position (1-9) for your move: ")) - 1
            if board[move] == " ":
                board[move] = 'X'
                print_board(board)
                break
            else:
                print("That position is already taken, try again.")
        except (ValueError, IndexError):
            print("Invalid move! Please enter a number between 1 and 9.")

# Main game logic
def play_game():
    board = [" " for _ in range(9)]  # Initialize an empty board
    print_board(board)
    
    # Choose who goes first
    print("Wanna play a game of Tic-Tac-Toe? Enter (Y/N)")
    my_response = input().strip().upper()

    if my_response == 'Y':
        print("Heads or Tails for who goes first: Enter (H/T)")
        coin_flip = input().strip().upper()

        if coin_flip == 'H' or coin_flip == 'T':
            print(f"You chose {coin_flip}, flipping the coin...")
            flip_result = random.choice(['H', 'T'])
            print(f"The coin landed on {flip_result}")

            if flip_result == coin_flip:
                print("You win the coin flip! You go first!")
                player_turn = True
            else:
                print("The other player wins the coin flip. They go first!")
                player_turn = False
        else:
            print("Invalid input! Please Enter: (H/T) for heads or tails.")
            return

        # Game loop
        for turn in range(9):
            if player_turn:
                player_move(board)
                if check_winner(board, 'X'):
                    print("You win!")
                    break
            else:
                computer_move(board)
                if check_winner(board, 'O'):
                    print("Computer wins!")
                    break

            player_turn = not player_turn  # Switch turn

        else:
            print("It's a draw!")

        # Ask for a rematch
        print("Wanna rematch? (Y/N)")
        rematch = input().strip().upper()
        if rematch == 'Y':
            play_game()
        else:
            print("Thanks for playing! Goodbye.")

    elif my_response == 'N':
        print("Well, that sucks! Goodbye!")
    else:
        print("Invalid input! Please Enter: (Y/N)")

# Run the game
play_game()
