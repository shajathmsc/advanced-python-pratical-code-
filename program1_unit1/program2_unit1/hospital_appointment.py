slots = 5

while True:
    print("\n1. Book Appointment")
    print("2. Check Available Slots")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if slots > 0:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))

            if age < 0 or age > 120:
                print("Invalid Age")
        else:
            print("No Appointments Available")
            continue

        if slots > 0 and 0 <= age <= 120:
            slots -= 1
            print("Appointment Booked for", name)

    elif choice == 2:
        print("Available Slots:", slots)

    elif choice == 3:
        if slots < 5:
            slots += 1
            print("Appointment Cancelled")
        else:
            print("No Appointment to Cancel")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid Choice")