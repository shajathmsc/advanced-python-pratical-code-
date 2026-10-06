class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.issued = False

    def display(self):
        print("book name:", self.book name)
        print("author:", self.author)

class User:
    def __init__(self, name):
        self.name = name

class Student(User):
    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(self.name, "issued", book.name)
        else:
            print("Book already issued")

    def return_book(self, book):
        if book.issued:
            book.issued = False
            print(self.name, "returned", book.name)
        else:
            print("Book is available")

book1 = Book("Python Programming", "Guido van Rossum")
student1 = Student("Arun")

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Display Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter choice: ")
    print("You selected:", repr(choice))

    if choice == "1":
        book1.display()

    elif choice == "2":
        student1.issue_book(book1)

    elif choice == "3":
        student1.return_book(book1)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice")