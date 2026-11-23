students = {}

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        marks = input("Enter marks: ")

        students[sid] = {"name": name, "marks": marks}
        print("Student added successfully")

    elif choice == 2:
        for sid, details in students.items():
            print(sid, details)

    elif choice == 3:
        sid = input("Enter student ID: ")
        if sid in students:
            print(students[sid])
        else:
            print("Student not found")

    elif choice == 4:
        sid = input("Enter student ID: ")
        if sid in students:
            students[sid]["name"] = input("Enter new name: ")
            students[sid]["marks"] = input("Enter new marks: ")
            print("Student updated")
        else:
            print("Student not found")

    elif choice == 5:
        sid = input("Enter student ID: ")
        if sid in students:
            del students[sid]
            print("Student deleted")
        else:
            print("Student not found")

    elif choice == 6:
        break

    else:
        print("Invalid choice")