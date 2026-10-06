class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.name)
        print("Salary: Rs.", self.salary)


employees = []

while True:
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        emp_id = input("Enter employee ID: ")
        name = input("Enter employee name: ")
        salary = input("Enter salary: ")

        emp = Employee(emp_id, name, salary)
        employees.append(emp)
        print("Employee added successfully!")

    elif choice == "2":
        if len(employees) == 0:
            print("No employees available!")
        else:
            for emp in employees:
                emp.display()
                print("--------------------")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")