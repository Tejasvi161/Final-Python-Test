books = {}

while True:
    print("\n1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        books[title] = "Available"
        print("Book added")

    elif choice == 2:
        print("Available Books:")
        for title, status in books.items():
            if status == "Available":
                print(title)

    elif choice == 3:
        title = input("Enter book title: ")
        if title in books and books[title] == "Available":
            books[title] = "Issued"
            print("Book issued")
        else:
            print("Book not available")

    elif choice == 4:
        title = input("Enter book title: ")
        if title in books and books[title] == "Issued":
            books[title] = "Available"
            print("Book returned")
        else:
            print("Invalid book")

    elif choice == 5:
        title = input("Enter book title: ")
        if title in books:
            print(title, "-", books[title])
        else:
            print("Book not found")

    elif choice == 6:
        break

    else:
        print("Invalid choice")