import numpy as np
import pandas as pd

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Expense": [2000, 2500, 1800, 3000, 2200]
}

df = pd.DataFrame(data)

print("MONTHLY EXPENSES")
print(df)

print("\nTotal Expense:", np.sum(df["Expense"]))
print("Average Expense:", np.mean(df["Expense"]))
print("Maximum Expense:", np.max(df["Expense"]))
print("Minimum Expense:", np.min(df["Expense"]))