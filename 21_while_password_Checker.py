correct_password = "python123"

# Keep asking until the correct password is entered
while True:
    password = input("Enter password: ")

    if password == correct_password:
        print("Correct password!")
        break
    else:
        print("Incorrect password. Try again.")