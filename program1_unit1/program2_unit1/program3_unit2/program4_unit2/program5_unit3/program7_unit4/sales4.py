import numpy as np
import pandas as pd

data = {
    "Employee": ["Arun", "Bala", "Kumar", "Ravi", "Siva"],
    "Salary": [20000, 25000, 30000, 22000, 28000]
}

df = pd.DataFrame(data)

print("EMPLOYEE SALARY")
print(df)

print("\nTotal Salary:", np.sum(df["Salary"]))
print("Average Salary:", np.mean(df["Salary"]))
print("Highest Salary:", np.max(df["Salary"]))
print("Lowest Salary:", np.min(df["Salary"]))
print("\nSalary above 25000:")
print(df[df["Salary"] > 25000])