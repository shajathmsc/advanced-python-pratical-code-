print("===== STUDENT GRADE ANALYZER =====")

name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

total = 0
passed = True

for i in range(1, n + 1):
    mark = int(input("Enter mark for subject " + str(i) + ": "))

    if mark < 0 or mark > 100:
        print("Invalid mark! Enter marks between 0 and 100.")
        passed = False
        break

    total += mark

    if mark < 35:
        passed = False

if passed:
    average = total / n

    print("\n===== STUDENT REPORT =====")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average:", average)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)

    if average >= 50:
        print("Result: PASS")
    else:
        print("Result: FAIL")

else:
    print("Result: FAIL or Invalid Marks")

print("============================")

