old_password = "Welcome123"

entered = input("Enter old password: ")

if entered == old_password:
    new_password = input("Enter new password: ")

    if len(new_password) >= 8 and any(ch.isdigit() for ch in new_password):
        encrypted = ""

        for ch in new_password:
            encrypted += chr(ord(ch) + 2)

        with open("new_password.txt", "w") as file:
            file.write(encrypted)

        print("Password Changed Successfully")
        print("Encrypted Password:", encrypted)
    else:
        print("New password is weak")
else:
    print("Incorrect old password")