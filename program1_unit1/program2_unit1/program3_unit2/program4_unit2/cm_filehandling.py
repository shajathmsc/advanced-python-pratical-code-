def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    with open("contacts.txt", "a") as f:
        f.write(name + "," + phone + "," + email + "\n")

    print("Contact added successfully")

def display_contacts():
    try:
        with open("contacts.txt", "r") as f:
            print("\nContact Details:")
            print(f.read())
    except FileNotFoundError:
        print("No contacts available")

while True:
    print("\n1. Add Contact")
    print("2. Display Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        display_contacts()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")