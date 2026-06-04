students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter age: ")

        student = {
            "name": name,
            "age": age
        }

        students.append(student)
        print("Student added successfully!")

    # View Students
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nStudent List:")
            for student in students:
                print(f"Name: {student['name']}, Age: {student['age']}")

    # Search Student
    elif choice == "3":
        search_name = input("Enter student name to search: ")

        found = False

        for student in students:
            if student["name"].lower() == search_name.lower():
                print(f"Found: Name: {student['name']}, Age: {student['age']}")
                found = True
                break

        if not found:
            print("Student not found.")

    # Update Student
    elif choice == "4":
        update_name = input("Enter student name to update: ")

        found = False

        for student in students:
            if student["name"].lower() == update_name.lower():
                new_name = input("Enter new name: ")
                new_age = input("Enter new age: ")

                student["name"] = new_name
                student["age"] = new_age

                print("Student updated successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Delete Student
    elif choice == "5":
        delete_name = input("Enter student name to delete: ")

        found = False

        for student in students:
            if student["name"].lower() == delete_name.lower():
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found.")

    # Exit
    elif choice == "6":
        print("Thank you for using Student Management System!")
        break

    # Invalid Choice
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
