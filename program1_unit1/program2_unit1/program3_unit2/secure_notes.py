note = input("Enter your secret note: ")
key = 2

encrypted = ""

for ch in note:
    encrypted += chr(ord(ch) + key)

with open("notes.txt", "a") as file:
    file.write(encrypted + "\n")

print("Original Note:", note)
print("Encrypted Note:", encrypted)
print("Secret note saved successfully")