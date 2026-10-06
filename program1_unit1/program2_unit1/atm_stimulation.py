print("===== ATM SIMULATION SYSTEM =====")

balance = 5000

while True:
    print("\n1. Balance Inquiry")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Available Balance: Rs.", balance)

    elif choice == 2:
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance = balance + amount
            print("Deposit Successful!")
            print("Updated Balance: Rs.", balance)
        else:
            print("Invalid Amount!")

    elif choice == 3:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid Amount!")
        elif amount > balance:
            print("Insufficient Balance!")
        else:
            balance = balance - amount
            print("Withdrawal Successful!")
            print("Updated Balance: Rs.", balance)

    elif choice == 4:
        print("Thank you for using ATM!")
        break

    else:
        print("Invalid Choice! Try Again.")

print("===== TRANSACTION ENDED =====")
