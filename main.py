from student_management import Student, StudentManagementSystem


def show_menu() -> None:
    print("\nStudent Management System")
    print("1. Add student")
    print("2. View all students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search student")
    print("0. Exit")


def main() -> None:
    system = StudentManagementSystem()

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            student_id = input("Student ID: ").strip()
            name = input("Name: ").strip()
            age = int(input("Age: ").strip())
            course = input("Course: ").strip()
            student = Student(student_id=student_id, name=name, age=age, course=course)
            system.add_student(student)
            print("Student added successfully.")

        elif choice == "2":
            students = system.list_students()
            if not students:
                print("No students found.")
            else:
                for student in students:
                    print(f"{student.student_id} | {student.name} | {student.age} | {student.course}")

        elif choice == "3":
            student_id = input("Student ID to update: ").strip()
            name = input("New name (leave blank to keep): ").strip()
            age_input = input("New age (leave blank to keep): ").strip()
            course = input("New course (leave blank to keep): ").strip()

            updates = {}
            if name:
                updates["name"] = name
            if age_input:
                updates["age"] = int(age_input)
            if course:
                updates["course"] = course

            if system.update_student(student_id, **updates):
                print("Student updated successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            student_id = input("Student ID to delete: ").strip()
            if system.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "5":
            student_id = input("Student ID to search: ").strip()
            student = system.get_student(student_id)
            if student:
                print(f"Found: {student.name} | {student.age} | {student.course}")
            else:
                print("Student not found.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
