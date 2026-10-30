"""a class attribute that counts employees created"""
class Employee:
    count = 0

    def __init__(self, name,position):
        self.name = name
        self.position = position
        Employee.count += 1
    def show_details(self):
        print("Employee Name:", self.name)
        print("Position:", self.position)
e1 = Employee("Akshada","HR")
e2 = Employee("Rahul","Sr.Engineer")
e3 = Employee("Priya","Jr.Engineer")
e1.show_details()
e2.show_details()
e3.show_details()

print("Total Employees:", Employee.count)
