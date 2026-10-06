contacts = {
    "Arun": ["9876543210", "arun@gmail.com"],
    "Priya": ["9876501234", "priya@gmail.com"]
}

name = input("Enter name to delete: ")

if name in contacts:
    del contacts[name]
    print("Contact deleted successfully")
else:
    print("Contact not found")

print(contacts) 