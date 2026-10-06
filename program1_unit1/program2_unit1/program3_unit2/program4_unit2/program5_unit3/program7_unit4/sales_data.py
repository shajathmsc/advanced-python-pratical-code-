import numpy as np
import pandas as pd

# Read CSV file
df = pd.read_csv("sales.csv")

# Calculate total sales
df["Total"] = df["Quantity"] * df["price"]

print("SALES DATA")
print(df)

# NumPy calculations
sales = np.array(df["Total"])

print("\nTotal Sales:", np.sum(sales))
print("Average Sales:", np.mean(sales))
print("Highest Sales:", np.max(sales))
print("Lowest Sales:", np.min(sales))

# Best selling product
best = df.loc[df["Total"].idxmax()]

print("\nBest Selling Product:", best["product"])