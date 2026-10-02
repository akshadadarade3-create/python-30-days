lists = {
    "student1":{
        "name" : "akshuu",
        "marks" : [88,72,83]
    },
    "student2" : {
        "name" : "anu",
        "marks" : [75,81,73]
    },
    "student3" : {
        "name" : "sakhi",
        "marks" : [76,70,71]
    }
}
for student in lists.values():
    name = student["name"]
    marks = student["marks"]

    average = sum(marks) / len(marks)

    print(f"{name} Average: {average:.2f}")

