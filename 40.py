tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("6. View Completed Tasks")
    print("7. View Pending Tasks")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append({"task": task, "status": "Pending"})
        print("Task added")

    elif choice == 2:
        for i, t in enumerate(tasks):
            print(i + 1, t)

    elif choice == 3:
        n = int(input("Enter task number: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["task"] = input("Enter new task: ")
            print("Task updated")
        else:
            print("Invalid task number")

    elif choice == 4:
        n = int(input("Enter task number: "))
        if 1 <= n <= len(tasks):
            tasks.pop(n-1)
            print("Task deleted")
        else:
            print("Invalid task number")

    elif choice == 5:
        n = int(input("Enter task number: "))
        if 1 <= n <= len(tasks):
            tasks[n-1]["status"] = "Completed"
            print("Task completed")
        else:
            print("Invalid task number")

    elif choice == 6:
        for t in tasks:
            if t["status"] == "Completed":
                print(t)

    elif choice == 7:
        for t in tasks:
            if t["status"] == "Pending":
                print(t)

    elif choice == 8:
        break

    else:
        print("Invalid choice")