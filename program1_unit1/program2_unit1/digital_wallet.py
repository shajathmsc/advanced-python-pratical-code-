balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Add Money")
    print("3. Send Money")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Wallet Balance:", balance)

    elif choice == 2:
        amount = int(input("Enter amount: "))

        if amount > 0:
            balance += amount
            print("Money Added Successfully")
        else:
            print("Invalid Amount")

    elif choice == 3:
        amount = int(input("Enter amount to send: "))

        if amount <= 0:
            print("Invalid Amount")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Money Sent Successfully")
            print("Remaining Balance:", balance)

    elif choice == 4:
        print("Wallet Closed")
        break

    else:
        print("Invalid Choice")

