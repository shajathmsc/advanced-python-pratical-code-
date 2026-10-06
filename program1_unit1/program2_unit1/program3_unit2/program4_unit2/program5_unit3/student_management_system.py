students = {}

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Display Students")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        roll = input("Enter roll number: ")
        name = input("Enter name: ")
        mark = input("Enter mark: ")
        students[roll] = [name, mark]
        print("Student added successfully")

    elif choice == "2":
        roll = input("Enter roll number: ")
        if roll in students:
            print("Name:", students[roll][0])
            print("Mark:", students[roll][1])
        else:
            print("Student not found")

    elif choice == "3":
        for roll, details in students.items():
            print(roll, details[0], details[1])

    elif choice == "4":
        print("Thank you")
        break

    else:
        print("Invalid choice")