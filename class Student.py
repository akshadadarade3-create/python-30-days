class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def average(self):
        return sum(self.marks)/len(self.marks)
    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

student1 = student("Akshada", [87,88,76])
student2 = student("sakhi", [85, 90, 80])
student3 = student("Rahul", [65, 70, 60])

print("Student:", student1.name)
print("Average:", student1.average())
print("Grade:", student1.grade())
print()
print("Student:", student2.name)
print("Average:", student2.average())
print("Grade:", student2.grade())
print()
print("Student:", student3.name)
print("Average:", student3.average())
print("Grade:", student3.grade())

