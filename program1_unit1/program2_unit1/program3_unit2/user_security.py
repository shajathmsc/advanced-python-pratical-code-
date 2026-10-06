username = input("Enter username: ")
password = input("Create password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    encrypted = ""

    for ch in password:
        encrypted += chr(ord(ch) + 2)

    with open("user_data.txt", "a") as file:
        file.write(username + ":" + encrypted + "\n")

    print("Account Created Successfully")
    print("Encrypted Password:", encrypted)
    print("Data saved to file")

else:
    print("Password must have 8 characters and a digit")