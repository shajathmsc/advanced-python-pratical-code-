password = input("Enter your password: ")

if len(password) < 8:
    print("Weak Password: Minimum 8 characters required")
else:
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        print("Strong Password")

        encrypted = ""
        for ch in password:
            encrypted += chr(ord(ch) + 3)

        with open("password.txt", "a") as file:
            file.write(encrypted + "\n")

        print("Encrypted Password:", encrypted)
        print("Saved to password.txt")

    else:
        print("Weak Password")
        print("Use uppercase, lowercase, digit and special character")