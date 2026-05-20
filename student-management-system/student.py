from file_handler import read_students, write_students
from utils import calculate_percentage

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")

    marks = []
    total = 0

    for i in range(3):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
        total += mark

    percentage = calculate_percentage(total, 300)

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "percentage": percentage
    }

    students = read_students()
    students.append(student)
    write_students(students)

    print("Student added successfully!")

def view_students():
    students = read_students()

    if not students:
        print("No student records found.")
        return

    for student in students:
        print("\n----------------------")
        print("Name:", student["name"])
        print("Roll:", student["roll"])
        print("Marks:", student["marks"])
        print("Percentage:", student["percentage"], "%")

def search_student():
    roll = input("Enter roll number to search: ")

    students = read_students()

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Percentage:", student["percentage"], "%")
            return

    print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")

    students = read_students()

    for student in students:
        if student["roll"] == roll:
            new_name = input("Enter new name: ")
            student["name"] = new_name

            write_students(students)

            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter roll number to delete: ")

    students = read_students()

    updated_students = [
        student for student in students
        if student["roll"] != roll
    ]

    write_students(updated_students)

    print("Student deleted successfully!")