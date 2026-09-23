correct_user = "admin"
correct_pass = "admin123"

attempts = 3
login_success = False

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_user and password == correct_pass:
        login_success = True
        print("\nLogin successful! Welcome to the system.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Invalid credentials. Attempts left: {attempts}\n")
        else:
            print("\nAccount locked! You have exceeded the maximum 3 attempts.")
