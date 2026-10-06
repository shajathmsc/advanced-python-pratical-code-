contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts[name] = [phone, email]
    print("Contact added successfully")

def display_contacts():
    for name, details in contacts.items():
        print(name, details[0], details[1])

add_contact()
display_contacts()
