import random

# Start the game loop
while True:
    question = input('Do you want to play Rock, Paper, Scissors? ').strip().lower()

    if question != 'yes':
        print('Alright, maybe next time!')
        break  # Exit the game if the user says no

    # Ask who will go first
    answer = input('Would you like to say the cadence first, or shall I? (Type "I will go first" or "You go ahead"): ').strip()

    if answer.lower() == 'i will go first':
        user_choice = input('Your turn! Choose Rock, Paper, or Scissors: ').strip().capitalize()
        if user_choice not in ['Rock', 'Paper', 'Scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        print(f'I chose: {computer_choice}')
    elif answer.lower() == 'you go ahead':
        computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
        print(f'I chose: {computer_choice}')
        user_choice = input('Your turn! Choose Rock, Paper, or Scissors: ').strip().capitalize()
        if user_choice not in ['Rock', 'Paper', 'Scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue
    else:
        print("Invalid response. Please try again.")
        continue

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        print("You win!")
    else:
        print("I win!")

    # Ask for a rematch
    rematch = input('Do you want a rematch? (yes/no): ').strip().lower()
    if rematch != 'yes':
        print('Thanks for playing! Goodbye!')
        break


