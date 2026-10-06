import matplotlib.pyplot as plt

expenses = [2000, 1500, 1000, 2500, 3000]
categories = ["Food", "Travel", "Books", "Rent", "Other"]

plt.pie(expenses, labels=categories, autopct="%1.1f%%")
plt.title("Monthly Expenses")
plt.savefig("chart.png")
plt.show()