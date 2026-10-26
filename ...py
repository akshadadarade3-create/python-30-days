# Add full error handling to your Stage 2 Student Records Manager.
students = []
class DuplicateRollNumberError(Exception):
    pass
class StudentNotFoundError(Exception):
    pass
class InvalidMarksError(Exception):
    pass
def validate_marks(marks):
    for mark in marks:
        if mark <= 0 or mark >= 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
def add_student():
    roll_no = input("Enter Roll Number: ").strip()
    if not roll_no:
        raise ValueError("Roll number cannot be empty.")
    for student in students:
        if student["roll_no"] == roll_no:
            raise DuplicateRollNumberError("Roll number already exists.")
    name = input("Enter student name: ").strip()
    if not name:
        raise ValueError("Student name cannot be empty.")
    marks = []
    for i in range(3):
        mark = int(input(f"Enter marks for Subject {i + 1}: "))
        marks.append(mark)

    validate_marks(marks)
    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": marks
        }
    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
        return
    print(f"{'Roll No':<10}{'Name':<15}"f"{'Subject 1':<12}{'Subject 2':<12}"f"{'Subject 3':<12}{'Total':<10}")

    for student in students:
        try:
            total = sum(student["marks"])
            print(f"{student['roll_no']:<10}",f"{student['name']:<15}", f"{student['marks'][0]:<12}", f"{student['marks'][1]:<12}",f"{student['marks'][2]:<12}",f"{total:<10}")
        except KeyError as error:
            print("Incomplete student record:", error)

def search_student():
    search_value = input("Enter Roll Number or Student Name to Search: ").strip()
    if not search_value:
        raise ValueError("Search input cannot be empty.")
    for student in students:
        if (student["roll_no"] == search_value or student["name"].lower() == search_value.lower()):
            print("Student Found!\nRoll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", sum(student["marks"]))
            return
    raise StudentNotFoundError("Student not found!")
def update_marks():
    roll_no = input("Enter Roll no of Student to Update: ").strip()
    if not roll_no:
        raise ValueError("Roll number cannot be empty.")
    for student in students:
        if student["roll_no"] == roll_no:
            marks = []

            for i in range(3):
                mark = int(input(f"Enter new marks for Subject {i + 1}: "))
                marks.append(mark)
            validate_marks(marks)

            student["marks"] = marks
            print("Marks updated successfully!")
            return
    raise StudentNotFoundError("Student not found!")

def delete_student():
    roll_no = input("Enter roll no to delete: ").strip()
    if not roll_no:
        raise ValueError("Roll number cannot be empty.")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return
    raise StudentNotFoundError("Student not found!")

def show_statistics():
    if len(students) == 0:
        print("No student records available.")
        return
    topper = max(students,key=lambda student: sum(student["marks"]))
    print("\nClass Topper:", topper["name"])
    print("Roll Number:", topper["roll_no"])
    print("Total Marks:", sum(topper["marks"]))

    total_marks = 0
    for student in students:
        total_marks += sum(student["marks"])
    class_average = total_marks / (len(students) * 3)
    print("Class Average:", round(class_average, 2))

while True:
    print("\n1. Add Student\n2. View Students\n3. Search Student\n4. Update Marks\n5. Delete Student\n6. Show Class Topper and Average\n7. Exit")
    try:
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("Thank you")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 7.")

    except ValueError as error:
        print("Input Error:", error)
    except InvalidMarksError as error:
        print("Marks Error:", error)
    except DuplicateRollNumberError as error:
        print("Duplicate Error:", error)
    except StudentNotFoundError as error:
        print("Search Error:", error)
    finally:
        print("Operation finished.")
