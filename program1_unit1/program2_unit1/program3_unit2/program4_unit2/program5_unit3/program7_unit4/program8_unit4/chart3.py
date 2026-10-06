import matplotlib.pyplot as plt

employees = ["Arun", "Bala", "Kumar", "Ravi", "Siva"]
salary = [20000, 25000, 30000, 22000, 28000]

plt.bar(employees, salary)
plt.title("Employee Salary Comparison")
plt.xlabel("Employees")
plt.ylabel("Salary (Rs.)")
plt.savefig("chart.png")
plt.show()