while True:
    print("\nCalculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Calculator closed.")
        break

    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", number1 + number2)

    elif choice == 2:
        print("Result:", number1 - number2)

    elif choice == 3:
        print("Result:", number1 * number2)

    elif choice == 4:
        if number2 != 0:
            print("Result:", number1 / number2)
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid choice.")