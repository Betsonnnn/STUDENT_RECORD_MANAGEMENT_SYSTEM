students = []

# Function to calculate grade


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 75:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to add student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    # Prevent duplicate roll numbers
    for student in students:
        if student["roll"] == roll:
            print("Roll number already exists!")
            return

    marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5
    grade = calculate_grade(average)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)
    print("Student added successfully!\n")


# Function to view all students
def view_students():
    if not students:
        print("No students available.\n")
        return

    for student in students:
        print("\n----------------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", round(student["average"], 2))
        print("Grade:", student["grade"])
    print()


# Function to search student
def search_student():
    roll = input("Enter roll number to search: ")
    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found:")
            print(student)
            return
    print("Student not found.\n")


# Function to show class statistics
def class_statistics():
    if not students:
        print("No students available.\n")
        return

    total_students = len(students)
    class_average = sum(s["average"] for s in students) / total_students

    highest = max(students, key=lambda x: x["total"])
    lowest = min(students, key=lambda x: x["total"])

    print("\nClass Statistics")
    print("Total Students:", total_students)
    print("Class Average:", round(class_average, 2))
    print("Highest Scorer:", highest["name"], "-", highest["total"])
    print("Lowest Scorer:", lowest["name"], "-", lowest["total"])
    print()


# Main menu
def menu():
    while True:
        print("----- Student Record System -----")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Class Statistics")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


# Run program
menu()
