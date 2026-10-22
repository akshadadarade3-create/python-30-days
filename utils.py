def average(*args):
    if len(args) == 0:
        return None
    return sum(args) / len(args)

def factorial(n):
    if n < 0:
        raise ValueError("Number cannot be negative.")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])

def reverse_string(text):
    if len(text) <= 1:
        return text
    return reverse_string(text[1:]) + text[0]

if __name__ == "__main__":
    print("Testing utils.py")
    