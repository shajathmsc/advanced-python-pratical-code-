contacts = {
    "Arun": ["9876543210", "arun@gmail.com"],
    "Priya": ["9876501234", "priya@gmail.com"]
}

name = input("Enter name to search: ")

if name in contacts:
    print("Phone:", contacts[name][0])
    print("Email:", contacts[name][1])
else:
    print("Contact not found")