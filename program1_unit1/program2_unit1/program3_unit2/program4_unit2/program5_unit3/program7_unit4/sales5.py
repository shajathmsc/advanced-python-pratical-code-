import numpy as np
import pandas as pd

data = {
    "Product": ["Pen", "Book", "Bag", "Box", "Pencil"],
    "Stock": [50, 20, 5, 15, 40]
}

df = pd.DataFrame(data)

print("PRODUCT STOCK")
print(df)

print("\nTotal Stock:", np.sum(df["Stock"]))
print("Average Stock:", np.mean(df["Stock"]))
print("Maximum Stock:", np.max(df["Stock"]))
print("Minimum Stock:", np.min(df["Stock"]))
print("\nLow Stock Products:")
print(df[df["Stock"] < 20])