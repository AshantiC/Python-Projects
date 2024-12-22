import random  # Import the random module for generating numbers

print("Welcome to the Guessing Game!")
while True:  # Infinite loop; will only exit if the user chooses 'N'
    print("\nI'm thinking of a number between 1 and 1000.")
    number_to_guess = random.randint(1, 1000)  # Computer generates a random number
    
    user_guess = None  # Initialize the user's guess
    while user_guess != number_to_guess:  # Keep asking until they guess correctly
        try:
            user_guess = int(input("Take a guess: "))  # Ask the user for a guess
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed it!")
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer input

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (Y/N): ").strip().lower()
    if play_again != 'y':  # Exit the game if the user doesn't input 'Y'
        print("Thanks for playing! Goodbye!")
        break




     

