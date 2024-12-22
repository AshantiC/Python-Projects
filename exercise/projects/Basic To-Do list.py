# Function to add to the to-do list
def list_add():
    print("What would you like to add?")
    user_input = input()  # Get input from the user
    with open('list.txt', 'a') as file:
        file.write(user_input + '\n')  # Append the input to the file
    print("Item added successfully!")

# Function to display the to-do list
def list_view():
    print("Current content of the to-do list:")
    try:
        with open('list.txt', 'r') as file:
            lines = file.readlines()
        if not lines:
            print("Your to-do list is empty!")
        else:
            for index, line in enumerate(lines, start=1):
                print(f"{index}: {line.strip()}")
    except FileNotFoundError:
        print("The to-do list file does not exist. Add something to create it!")

# Function to delete from the to-do list
def list_delete():
    list_view()  # Show the current list first
    print("Enter the number of the line you would like to delete:")
    try:
        with open('list.txt', 'r') as file:
            lines = file.readlines()
        line_number = int(input())  # Get the line number from the user
        if 1 <= line_number <= len(lines):
            del lines[line_number - 1]  # Remove the selected line
            with open('list.txt', 'w') as file:
                file.writelines(lines)
            print("Line deleted successfully.")
        else:
            print("Invalid line number.")
    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("The to-do list file does not exist. Nothing to delete!")

# Function to exit the program
def list_exit():
    print("Thank you for using the To-Do list application. Goodbye!")
    exit()

# Main menu
def main_menu():
    while True:
        print("\nWelcome to your To-Do list!")
        print("Please type 'ADD', 'DELETE', 'VIEW', or 'EXIT'")
        my_response = input().strip().upper()  # Normalize input to uppercase

        if my_response == "ADD":
            list_add()
        elif my_response == "DELETE":
            list_delete()
        elif my_response == "VIEW":
            list_view()
        elif my_response == "EXIT":
            list_exit()
        else:
            print("Invalid option. Please type 'ADD', 'DELETE', 'VIEW', or 'EXIT'.")

# Run the program
main_menu()