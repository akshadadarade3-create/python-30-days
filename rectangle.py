# Rewrite Rectangle as a @dataclass 
from dataclasses import dataclass
@dataclass
class Rectangle:
    length: float
    width: float
    def area(self):
        return self.length * self.width
r1 = Rectangle(10, 5)
print(r1)
print("Area:", r1.area())