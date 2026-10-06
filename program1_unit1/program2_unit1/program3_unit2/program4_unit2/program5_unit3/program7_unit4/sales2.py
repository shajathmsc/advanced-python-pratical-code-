import numpy as np
import pandas as pd

data = {
    "Student": ["Asha", "Banu", "Rani", "Priya", "Sara"],
    "Marks": [85, 90, 75, 95, 80]
}

df = pd.DataFrame(data)

print("STUDENT MARKS")
print(df)

print("\nTotal Marks:", np.sum(df["Marks"]))
print("Average Marks:", np.mean(df["Marks"]))
print("Highest Marks:", np.max(df["Marks"]))
print("Lowest Marks:", np.min(df["Marks"]))
print("Students scoring above 80:")
print(df[df["Marks"] > 80])