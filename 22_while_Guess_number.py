secret_number = 7

# Keep asking until the correct number is guessed
while True:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct! You guessed it.")
        break
    else:
        print("Wrong guess. Try again.")