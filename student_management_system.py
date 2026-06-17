import json
import os

FILE_NAME = "students.json"


# Load students from JSON file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []


# Save students to JSON file
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Load existing data
students = load_students()

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Student List")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Show Complete Details of All Students")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    # ADD STUDENT
    if choice == "1":

        student_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        course = input("Enter Course: ")
        department = input("Enter Department: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "gender": gender,
            "course": course,
            "department": department,
            "email": email,
            "phone": phone
        }

        students.append(student)
        save_students(students)

        print("\nStudent Added Successfully!")

    # VIEW STUDENT LIST
    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:
            print("\n========== STUDENT LIST ==========")

            for student in students:
                print(f"ID: {student['id']} | Name: {student['name']}")

    # SEARCH STUDENT
    elif choice == "3":

        search_name = input("Enter Student Name to Search: ")

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                print("\n========== STUDENT FOUND ==========")
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Gender     : {student['gender']}")
                print(f"Course     : {student['course']}")
                print(f"Department : {student['department']}")
                print(f"Email      : {student['email']}")
                print(f"Phone      : {student['phone']}")

                found = True
                break

        if not found:
            print("\nStudent Not Found!")

    # UPDATE STUDENT
    elif choice == "4":

        update_id = input("Enter Student ID to Update: ")

        found = False

        for student in students:

            if student["id"] == update_id:

                print("\nEnter New Details")

                student["name"] = input("Name: ")
                student["age"] = input("Age: ")
                student["gender"] = input("Gender: ")
                student["course"] = input("Course: ")
                student["department"] = input("Department: ")
                student["email"] = input("Email: ")
                student["phone"] = input("Phone Number: ")

                save_students(students)

                print("\nStudent Updated Successfully!")
                found = True
                break

        if not found:
            print("\nStudent Not Found!")

    # DELETE STUDENT
    elif choice == "5":

        delete_id = input("Enter Student ID to Delete: ")

        found = False

        for student in students:

            if student["id"] == delete_id:

                students.remove(student)

                save_students(students)

                print("\nStudent Deleted Successfully!")
                found = True
                break

        if not found:
            print("\nStudent Not Found!")

    # SHOW COMPLETE DETAILS
    elif choice == "6":

        if len(students) == 0:
            print("\nNo Students Available.")

        else:

            print("\n========== ALL STUDENT DETAILS ==========")

            for student in students:

                print("\n--------------------------------------")
                print(f"Student ID : {student['id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Gender     : {student['gender']}")
                print(f"Course     : {student['course']}")
                print(f"Department : {student['department']}")
                print(f"Email      : {student['email']}")
                print(f"Phone      : {student['phone']}")
                print("--------------------------------------")

    # EXIT
    elif choice == "7":

        print("\nThank You For Using Student Management System!")
        break

    # INVALID CHOICE
    else:
        print("\nInvalid Choice! Please Enter 1 to 7.")
