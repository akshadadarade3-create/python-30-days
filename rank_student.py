names = ["Akshada", "Ananya", "Rahul", "Neha"]
marks = [85, 95, 78, 90]

students = list(zip(names, marks))

ranked_students = sorted(
    students,
    key=lambda student: student[1],
    reverse=True
)

print("Student Ranking:")

for rank, student in enumerate(ranked_students, start=1):
    print(rank, student[0], "-", student[1])