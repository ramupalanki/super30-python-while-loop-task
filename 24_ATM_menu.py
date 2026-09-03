#initialization
balance = 10000

while True:
    print("\nATM Menu")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    #taking the choice from the user
    choice = int(input("Enter your choice: "))

    #checking the choice is 1 and displaying balance
    if choice == 1:
        print("Balance:", balance)

    #checking the choice is 2 and performing deposit
    elif choice == 2:
        amount = float(input("Enter deposit amount: "))
        #checking if the amount is greater than 0 and updating balance
        if amount > 0:
            balance = balance + amount
            print("Amount deposited successfully.")
            print("New balance:", balance)
        else: #checking if the amount is less than or equal to 0 and displaying invalid amount
            print("Invalid amount.")
    #checking the choice is 3 and performing withdrawal
    elif choice == 3:
        #  
        amount = float(input("Enter withdrawal amount: "))
        
        #checking if the amount is greater than 0 and less than or equal to balance and updating balance
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Please collect your cash.")
            print("Remaining balance:", balance)
        else:
            print("Insufficient balance or invalid amount.")
    #checking the choice is 4 and exiting the loop
    elif choice == 4:
        print("Thank you for using the ATM.")
        break
    # 
    else:
        print("Invalid choice. Please try again.")