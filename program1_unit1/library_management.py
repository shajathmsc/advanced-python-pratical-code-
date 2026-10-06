available_books = 5

while True:
    print("\n1. Issue Book")
    print("2. Return Book")
    print("3. Check Books")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if available_books > 0:
            available_books -= 1
            print("Book issued successfully")
        else:
            print("No books available")

    elif choice == 2:
        days = int(input("Enter late days: "))

        if days < 0:
            print("Invalid days")
            continue

        if days == 0:
            fine = 0
        elif days <= 5:
            fine = days * 2
        else:
            fine = days * 5

        available_books += 1

        print("Fine:", fine)
        print("Book returned successfully")

    elif choice == 3:
        print("Available books:", available_books)

    elif choice == 4:
        print("Library closed")
        break

    else:
        print("Invalid choice")
