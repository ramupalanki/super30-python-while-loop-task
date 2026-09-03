number = int(input("Enter a number: "))

# Initialization: start factorial at 1 and counter at 1.
factorial = 1
counter = 1

# Condition: continue while counter is less than or equal to number.
while counter <= number:
    factorial = factorial * counter

    # Update: increase counter so the loop eventually terminates.
    counter = counter + 1

print("Factorial:", factorial)
