""" write 10 students with marks to a CSV; read it back and print averages """
import csv
students = [
    ["akshada", 85],
    ["ovi", 78],
    ["sneha", 92],
    ["yadnya", 67],
    ["shradha", 88],
    ["dhanu", 74],
    ["neha", 95],
    ["Hari", 81],
    ["Isha", 90],
    ["Jemimah", 70]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks"])
    writer.writerows(students)

print("Student data saved!")


choice = input("Do you want to add a student? (yes/no): ")

if choice == "yes":
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))

    
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)

        students = []

        for row in reader:
            students.append([row[0], int(row[1])])

    
    students.append([name, marks])

    
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Marks"])
        writer.writerows(students)

    print("Student added!")

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    total = 0
    count = 0

    for row in reader:
        name = row[0]
        marks = int(row[1])

        print(name, "-", marks)

        total = total + marks
        count = count + 1

    average = total / count
    print("Average marks:", average)
