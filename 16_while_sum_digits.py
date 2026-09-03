number = int(input("Enter a number: "))

# Initialization: start the sum at 0.
total = 0

# Condition: continue while there are digits left in the number.
while number > 0:
    digit = number % 10
    total = total + digit

    # Update: remove the last digit so the loop can eventually terminate.
    number = number // 10

print("Sum of digits:", total)
