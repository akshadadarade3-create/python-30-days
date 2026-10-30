class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(7, 3)

print("Rectangle 1")
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())
print()
print("Rectangle 2")
print("Area:", rectangle2.area())
print("Perimeter:", rectangle2.perimeter())
