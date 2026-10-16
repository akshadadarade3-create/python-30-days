"""math_utils.py — is_prime(n), factorial(n), fibonacci(n) and gcd(a, b), each with a docstring"""
# multi line command : ignored
def is_prime():
    """this check whether number is prime or not , return true if prime otherwise false"""
# (docstring state what a function does can be printed sometimes)
    n = int(input("Enter Number to Check:"))
    if n<2:
        return False
    for divisor in range(2, n):
        if n % divisor == 0:
            return False
    return True
print(is_prime())

def factorial():
    """Return the factorial of a positive integer."""
    n = int(input("Enter Number To find Factorial:"))
    if n < 0:
        print("Factorial is not defined for negative integers.")
    result = 1
    for number in range(1, n + 1):
        result = result * number

    return result  
print (factorial())   


def fibonacci():
    """Return the first n numbers of the Fibonacci sequence."""
    n = int(input("Enter No:"))
    if n < 0:
        print("Number of terms cannot be negative.")
    sequence = []
    a = 0
    b = 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence
print(fibonacci())


def gcd(a, b):
    """Return the greatest common divisor of two integers."""
    a = abs(a)
    b = abs(b)

    while b != 0:
        a, b = b, a % b

    return a
print(gcd(14,28))