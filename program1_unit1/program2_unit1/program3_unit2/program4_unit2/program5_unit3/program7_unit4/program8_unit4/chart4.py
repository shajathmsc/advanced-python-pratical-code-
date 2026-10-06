import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [1000, 1500, 1200, 2000, 1800]

products = ["Pen", "Book", "Bag", "Box"]
quantity = [50, 30, 20, 40]

expenses = [2000, 1500, 1000, 2500]
categories = ["Food", "Travel", "Books", "Rent"]

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")

plt.subplot(1, 3, 2)
plt.bar(products, quantity)
plt.title("Product Quantity")

plt.subplot(1, 3, 3)
plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Expenses")

plt.tight_layout()
plt.savefig("chart.png")
plt.show()