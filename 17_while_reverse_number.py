number = int(input("Enter a number: "))

# Initialization: start the reversed number at 0.
reverse = 0

# Condition: continue while there are digits left in the number.
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit

    # Update: remove the last digit so the loop eventually terminates.
    number = number // 10

print("Reversed number:", reverse)
