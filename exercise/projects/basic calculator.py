print('Welcome to your calculator')

while True:
    num1 = int(input('Please enter a number: '))
    sign = input('Enter symbol (+, -, *, /): ')
    num2 = int(input('Please enter another number: '))

    if sign == "+" and num1 > 0 and num2 > 0:
        num3 = num1 + num2
        print('Your answer is', num3)

    elif sign == "-" and num1 > 0 and num2 > 0:
        num3 = num1 - num2
        print('Your answer is', num3)

    elif sign == "*" and num1 > 0 and num2 > 0:
        num3 = num1 * num2
        print('Your answer is', num3)

    elif sign == "/" and num1 > 0 and num2 > 0:
        if num2 != 0:
            num3 = num1 / num2
            print('Your answer is', num3)
        else:
            print("Division by zero is not allowed.")
    else:
        print("Invalid input or operation.")

    # Asking if the user wants to continue
    continue_choice = input('Do you want to continue? (yes/no): ').strip().lower()
    if continue_choice != 'yes':
        print('Goodbye!')
        break
