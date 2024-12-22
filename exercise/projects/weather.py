import weather

def main_menu():
    while True:
        print("\nWelcome to the Weather App!")
        print("What would you like to check:")
        print("1: Temperature")
        print("2: Forecast")
        print("3: Alerts")
        print("4: Exit")
        
        my_response = input("Please enter the number of your choice: ").strip().upper()
        
        if my_response == '1':
            print("The temperature outside is: [Fetch temperature here]")
        elif my_response == '2':
            print("Here is the weather forecast: [Fetch forecast here]")
        elif my_response == '3':
            print("Weather alerts: [Fetch alerts here]")
        elif my_response == '4':
            print("Thank you for using the Weather App. Goodbye!")
            break  # Exit the loop and program
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            