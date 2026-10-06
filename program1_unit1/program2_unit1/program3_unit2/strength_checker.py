password = input("Enter password: ")

upper = any(ch.isupper() for ch in password)
lower = any(ch.islower() for ch in password)
digit = any(ch.isdigit() for ch in password)
special = any(not ch.isalnum() for ch in password)

if len(password) >= 8 and upper and lower and digit and special:
    print("Very Strong Password")
elif len(password) >= 8 and upper and lower and digit:
    print("Strong Password")
else:
    print("Weak Password")

encrypted = ""

for ch in password:
    encrypted += chr(ord(ch) + 1)

print("Encrypted Password:", encrypted)