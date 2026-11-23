account = {}

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Display Details")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        account["name"] = input("Enter name: ")
        account["number"] = input("Enter account number: ")
        account["balance"] = 0
        print("Account created")

    elif choice == 2:
        if account:
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                account["balance"] += amount
                print("Money deposited")
            else:
                print("Invalid amount")
        else:
            print("Create an account first")

    elif choice == 3:
        if account:
            amount = float(input("Enter withdrawal amount: "))
            if 0 < amount <= account["balance"]:
                account["balance"] -= amount
                print("Money withdrawn")
            else:
                print("Invalid amount or insufficient balance")
        else:
            print("Create an account first")

    elif choice == 4:
        if account:
            print("Balance:", account["balance"])
        else:
            print("Create an account first")

    elif choice == 5:
        if account:
            print("Account details:", account)
        else:
            print("Create an account first")

    elif choice == 6:
        break

    else:
        print("Invalid choice")