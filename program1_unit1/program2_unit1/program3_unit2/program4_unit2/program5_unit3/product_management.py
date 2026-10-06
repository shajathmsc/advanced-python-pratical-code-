class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def display(self):
        print("Product ID:", self.product_id)
        print("Product Name:", self.name)
        print("Price: Rs.", self.price)


products = []

while True:
    print("\n===== PRODUCT MANAGEMENT =====")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))

        product = Product(product_id, name, price)
        products.append(product)
        print("Product added successfully!")

    elif choice == "2":
        if len(products) == 0:
            print("No products available!")
        else:
            for product in products:
                product.display()
                print("--------------------")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")