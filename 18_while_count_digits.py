number = int(input("Enter a number: "))

# Handle 0 separately because 0 is one digit.
if number == 0:
    count = 1
else:
    # Initialization: start the digit count at 0.
    count = 0

    # Condition: continue while there are digits left in the number.
    while number > 0:
        count = count + 1

        # Update: remove the last digit so the loop can eventually terminate.
        number = number // 10

print("Number of digits:", count)
