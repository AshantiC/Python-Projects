import random

# Function to select a random word
def select_word():
    words = ["python", "hangman", "programming", "developer", "challenge", "function"]
    return random.choice(words)

# Function to display the current game state
def display_game_state(displayed_word, attempts_left, incorrect_guesses):
    print("\nWord to guess: ", " ".join(displayed_word))
    print(f"Attempts left: {attempts_left}")
    print("Incorrect guesses: ", ", ".join(incorrect_guesses))

# Main game loop
def play_hangman():
    print("Welcome to Hangman!")
    
    while True:  # Restart the game until the user decides to quit
        word_to_guess = select_word()  # Select a random word
        displayed_word = ["_"] * len(word_to_guess)  # Mask the word
        correct_guesses = set()
        incorrect_guesses = []
        attempts_left = 6  # Max number of incorrect guesses
        
        print("\nLet's start the game!")
        
        # Inner game loop
        while attempts_left > 0:
            display_game_state(displayed_word, attempts_left, incorrect_guesses)
            user_guess = input("Guess a letter: ").lower()
            
            if len(user_guess) != 1 or not user_guess.isalpha():
                print("Please enter a single letter.")
                continue
            
            if user_guess in correct_guesses or user_guess in incorrect_guesses:
                print("You already guessed that letter!")
                continue
            
            # Check if the letter is in the word
            if user_guess in word_to_guess:
                print("Good guess!")
                correct_guesses.add(user_guess)
                # Update displayed word
                for i, letter in enumerate(word_to_guess):
                    if letter == user_guess:
                        displayed_word[i] = user_guess
            else:
                print("Wrong guess!")
                incorrect_guesses.append(user_guess)
                attempts_left -= 1
            
            # Check win condition
            if "_" not in displayed_word:
                print("\nCongratulations! You guessed the word:", word_to_guess)
                break
        
        # Check loss condition
        if attempts_left == 0:
            print("\nGame Over! The word was:", word_to_guess)
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing Hangman! Goodbye!")
            break

# Start the game
play_hangman()
