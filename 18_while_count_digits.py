number = int(input("Enter a number: "))

count = 0

# Continue until all digits are processed
while number > 0:
    count = count + 1

    # Remove the last digit
    number = number // 10

print("Number of digits:", count)