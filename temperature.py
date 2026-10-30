"""use @property to block values below absolute zero """
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            print("Invalid Temperature!")
        else:
            self._celsius = value
t1 = Temperature(25)
print("Temperature:", t1.celsius)
t1.celsius = 30
print("Updated Temperature:", t1.celsius)
t1.celsius = -300
print("Final Temperature:", t1.celsius)
