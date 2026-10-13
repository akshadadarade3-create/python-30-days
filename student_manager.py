"""Build a menu-driven student records system. Each student is a dictionary with a roll number, name, and marks 
for 3 subjects. 
REQUIREMENTS 
• Add a student — reject duplicate roll numbers ,View all students in a table ,Search by roll number or name
• Update marks; delete a student 
• Show the class topper and class average 
• Invalid menu input must never crash the program"""

students = []
def add_student():
   try : 
      roll_no = (input("Enter Roll Number:"))
   except ValueError:
      print("Invalid Roll Number")
      return
   for student in students:
        if student["roll_no"] == roll_no:
            print("Roll number already exists")
            return

   name = input("Enter student name: ")
   marks1 = int(input("Enter marks for Subject 1: "))
   marks2 = int(input("Enter marks for Subject 2: "))
   marks3 = int(input("Enter marks for Subject 3: "))

   student = {
        "roll_no": roll_no,
        "name": name,
        "marks": [marks1, marks2, marks3]
    }
   students.append(student)
   print("Student added successfully!")
"""sare students aur unke details"""
def view_students():
    if len(students) == 0:
        print("No student records found.")
        return

    print(f"{'Roll No':<10}{'Name':<15}{'Subject 1':<12}{'Subject 2':<12}{'Subject 3':<12}{'Total':<10}")

    for student in students:
        total = sum(student["marks"])

        print(
            f"{student['roll_no']:<10}"
            f"{student['name']:<15}"
            f"{student['marks'][0]:<12}"
            f"{student['marks'][1]:<12}"
            f"{student['marks'][2]:<12}"
            f"{total:<10}"
        )
"""students record search krne ke liye"""       
def search_student():
    search_value = input("Enter Roll Number or Student Name to Search: ").strip()

    for student in students:
        if student["roll_no"] == search_value or student["name"].lower() == search_value.lower():
            print("Student Found!")
            print("Roll No:", student["roll_no"])
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", sum(student["marks"]))
            return

    print("Student not found!")
"""marks update honge"""
def update_marks():
    roll_no = input("Enter Roll no of Students to Update:")
    for student in students:
        if student["roll_no"] == roll_no:
            marks = []

            for i in range(3):
                mark = int(input(f"Enter new marks for Subject {i + 1}: "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    return

                marks.append(mark)

            student["marks"] = marks
            print("Marks updated successfully!")
            return

    print("Student not found!")

def delete_student():
    roll_no = input("Enter roll no to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found!")

def show_statistics():
    if len(students) == 0:
        print("No student records available.")
        return

    topper = max(students, key=lambda student: sum(student["marks"]))

    print("\nClass Topper:", topper["name"])
    print("Roll Number:", topper["roll_no"])
    print("Total Marks:", sum(topper["marks"]))
    total_marks = 0
    for student in students:
        total_marks += sum(student["marks"])

    class_average = total_marks / (len(students) * 3)

    print("Class Average:", round(class_average, 2))

while True: 
    print("\n****STUDENT RECORDS MANAGER ****\n1. Add Student\n2. View All Students\n3. Search Student\n4. Update Marks\n5. Delete Student\n6. Show Class Topper and Average\n7. Exit")
    choice = input("Enter your choice: ")

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

