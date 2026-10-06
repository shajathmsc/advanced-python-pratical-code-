balance = 500

while True:
    print("\n1. Check Balance")
    print("2. Recharge")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance: Rs.", balance)

    elif choice == 2:
        amount = int(input("Enter recharge amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Recharge Successful!")
            print("Remaining Balance:", balance)
        elif amount <= 0:
            print("Invalid Amount")
        else:
            print("Insufficient Balance")

    elif choice == 3:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")

