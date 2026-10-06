name = input("Enter employee name: ")
salary = float(input("Enter basic salary: "))
attendance = int(input("Enter attendance days: "))

if salary <= 0 or attendance < 0 or attendance > 31:
    print("Invalid input")

else:
    if salary >= 50000:
        allowance = salary * 0.20
    elif salary >= 25000:
        allowance = salary * 0.15
    else:
        allowance = salary * 0.10

    if attendance >= 26:
        bonus = 2000
    else:
        bonus = 0

    if attendance < 20:
        deduction = 1000
    else:
        deduction = 0

    net_salary = salary + allowance + bonus - deduction

    print("Employee:", name)
    print("Allowance:", allowance)
    print("Bonus:", bonus)
    print("Deduction:", deduction)
    print("Net Salary:", net_salary)

