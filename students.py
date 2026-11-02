# Add  str  and  repr  to your Student class 
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"{self.name} scored {self.marks} marks"

    def __repr__(self):
        return f"Student('{self.name}', {self.marks})"

    def __lt__(self, other):
        return self.marks < other.marks

s1 = Student("Akshada", 90)
s2 = Student("sakhii", 85)
s3 = Student("Pihuu", 95)
students = [s1, s2, s3]
students.sort()
for student in students:
    print(student)