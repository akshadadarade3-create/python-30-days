"""invalidAgeError is the name of custom error.
(Exception) means your class inherits from Python's built-in Exception class"""
class InvalidAgeError(Exception):
    """Raised when an age is outside the valid range."""
    pass
def validate_age(age):
    if age < 0 or age > 120:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be between 0 and 120.")
    return True
try:
    age = int(input("Enter age: "))
    validate_age(age)
    print("Age is valid.")
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Please enter a valid integer.")
