#creating a basic chatbot that can answer simple questions or carry on a basic conversation
#this project going to need a define function(def), random module cause we want chatbot to say whatever he wants based
#on our response, we gonna need how many lengths of words chat bot can have.
#import a string since we generating random words or letters
#need to conversate between person 1 and 2
#person 1 and 2 needs to be define as a function

import random

# Function to fetch a random question from a file
def simple_questions():
    try:
        with open("questions.txt", "r") as file:
            questions = file.readlines()
        return random.choice(questions).strip()  # Strip any extra spaces or newline
    except FileNotFoundError:
        return "Questions file not found."

# Function for conversation when user chooses 'Y'
def conversation_yes():
    print("Awesome! Let's talk!")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        print(f"Bot: That sounds interesting! Tell me more about {user_input}.")

# Function for conversation when user chooses 'N'
def conversation_no():
    print("Alright! Let me ask you a random question.")
    while True:
        random_question = simple_questions()
        print(f"Bot: {random_question}")
        user_response = input("You: ").strip()
        if user_response.lower() == "exit":
            print("Goodbye! Have a great day!")
            break
        print(f"Bot: That's a great answer! Tell me more about your thoughts on that.")

# Main Chatbot loop
while True:
    print("Do you know what you would like to talk about? (Y/N or type 'exit' to quit)")
    my_response = input().strip().upper()  # Get input from the user and convert it to uppercase for uniformity

    if my_response == "EXIT":
        print("Goodbye! Have a great day!")
        break  # Exit the loop and end the program
    elif my_response == "Y":
        conversation_yes()  # Start the conversation for 'Y'
    elif my_response == "N":
        conversation_no()  # Start the conversation for 'N'
    else:
        print("I didn't understand that. Please type 'Y', 'N', or 'exit'.")  # Handle invalid input
