import json
import os

FILE = "students.json"

def load_students():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def add_student(students):
    print("ADD FUNCTION STARTED")
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    mark = input("Enter mark: ")

    students[roll] = [name, mark]
    save_students(students)
    print("Student added successfully")

def search_student(students):
    roll = input("Enter roll number to search: ")

    if roll in students:
        print("Name:", students[roll][0])
        print("Mark:", students[roll][1])
    else:
        print("Student not found")

def update_student(students):
    roll = input("Enter roll number to update: ")

    if roll in students:
        students[roll][0] = input("Enter new name: ")
        students[roll][1] = input("Enter new mark: ")
        save_students(students)
        print("Student updated successfully")
    else:
        print("Student not found")

def delete_student(students):
    roll = input("Enter roll number to delete: ")

    if roll in students:
        del students[roll]
        save_students(students)
        print("Student deleted successfully")
    else:
        print("Student not found")

def display_students(students):
    if not students:
        print("No students available")
    else:
        for roll, details in students.items():
            print(roll, details[0], details[1])

students = load_students()

while True:
    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Students")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        search_student(students)
    elif choice == "3":
        update_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        display_students(students)
    elif choice == "6":
        print("Students saved. Goodbye!")
        break
    else:
        print("Invalid choice")