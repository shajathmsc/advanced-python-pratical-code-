slots = 5
fee = 50

while True:
    print("\n1. Park Vehicle")
    print("2. Exit Vehicle")
    print("3. Check Slots")
    print("4. Exit Program")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if slots > 0:
            slots -= 1
            print("Vehicle Parked Successfully")
        else:
            print("Parking Full")

    elif choice == 2:
        if slots < 5:
            hours = int(input("Enter parking hours: "))

            if hours <= 0:
                print("Invalid Hours")
            else:
                print("Parking Fee:", hours * fee)
                slots += 1
                print("Vehicle Exited")
        else:
            print("No Vehicle Parked")

    elif choice == 3:
        print("Available Slots:", slots)

    elif choice == 4:
        break

    else:
        print("Invalid Choice")
