# Initialization: start with the first even number.
number = 2

# Condition: continue while number is less than or equal to 100.
while number <= 100:
    if number % 2 == 0:
        print(number)

    # Update: increase number by 1 so the loop eventually terminates.
    number = number + 1
