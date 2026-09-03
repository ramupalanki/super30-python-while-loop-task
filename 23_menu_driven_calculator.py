# Initialization: no counter is needed because the menu repeats until the user chooses Exit.
while True:
    # Condition: while True keeps the calculator menu running repeatedly.
    # Termination: the loop ends when the user chooses option 5 and break is executed.

    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # taking the choice from the user
    choice = int(input("Enter your choice: "))

    # checking if the choice is 5, if yes then exit the loop
    if choice == 5:
        print("Calculator closed.")
        break

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    # checking the choice is 1 and performing addition
    if choice == 1:
        print("Result:", number1 + number2)

    # checking the choice is 2 and performing subtraction
    elif choice == 2:
        print("Result:", number1 - number2)

    # checking the choice is 3 and performing multiplication
    elif choice == 3:
        print("Result:", number1 * number2)

    # checking the choice is 4 and performing division
    elif choice == 4:
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Cannot divide by zero.")

    # checking if the choice is not valid
    else:
        print("Invalid choice.")
