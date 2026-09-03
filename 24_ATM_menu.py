balance = 10000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully.")
            print("New balance:", balance)
        else:
            print("Invalid amount.")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == 4:
        print("Thank you for using the ATM.")
        break

    else:
        print("Invalid choice. Please try again.")