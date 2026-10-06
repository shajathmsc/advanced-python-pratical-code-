print("1. Pizza - Rs.200")
print("2. Burger - Rs.100")
print("3. Sandwich - Rs.80")

choice = int(input("Enter choice: "))
quantity = int(input("Enter quantity: "))

if quantity <= 0:
    print("Invalid quantity")

else:
    if choice == 1:
        price = 200
    elif choice == 2:
        price = 100
    elif choice == 3:
        price = 80
    else:
        price = 0

    if price == 0:
        print("Invalid choice")
    else:
        total = price * quantity

        if total >= 500:
            discount = total * 0.10
        else:
            discount = 0

        if total >= 300:
            delivery = 0
        else:
            delivery = 40

        bill = total - discount + delivery

        print("Food Total:", total)
        print("Discount:", discount)
        print("Delivery:", delivery)
        print("Final Bill:", bill)




