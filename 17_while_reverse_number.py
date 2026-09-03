number = int(input("Enter a number: "))

reverse = 0

# Continue until all digits are processed
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit

    # Remove the last digit
    number = number // 10

print("Reversed number:", reverse)