number = int(input("Enter a number: "))

factorial = 1
counter = 1

# Continue multiplying until counter reaches the number
while counter <= number:
    factorial = factorial * counter

    # Update
    counter = counter + 1

print("Factorial:", factorial)