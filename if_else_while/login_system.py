MAX_ATTEMPTS = 3
attempts = 0

while attempts < MAX_ATTEMPTS:
    password = input("Enter password: ")

    if password == "admin123":
        print("Login successful")
        break  # if we hit break, rest is skipped

    elif password == "":
        print("Password cannot be empty")

    else:
        print("--Wrong password--")

    attempts += 1

else:
    print("Too many attempts. Access blocked")
