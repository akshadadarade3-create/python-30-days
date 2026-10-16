"""conversion functions between Celsius, Fahrenheit and Kelvin """
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin."""
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius."""
    if kelvin < 0:
        raise ValueError("Kelvin cannot be below zero.")
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin."""
    kelvin = (fahrenheit - 32) * 5 / 9 + 273.15

    if kelvin < 0:
        raise ValueError("Temperature cannot be below zero.")
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit."""
    if kelvin < 0:
        raise ValueError("Kelvin cannot be below zero.")

    return (kelvin - 273.15) * 9 / 5 + 32

print(f"25°C to Fahrenheit:{celsius_to_fahrenheit(25):2f}")
print(f"77°F to Celsius:{fahrenheit_to_celsius(77):.2f}")
print(f"25°C to Kelvin:{celsius_to_kelvin(25):.2f}")
print(f"300 K to Celsius:{kelvin_to_celsius(300):.2f}")
print(f"77°F to Kelvin:{fahrenheit_to_kelvin(77):.2f}")
print(f"300 K to Fahrenheit:{kelvin_to_fahrenheit(300):.2f}")
