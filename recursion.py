def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)

def recursive_sum(numbers):
    if len(numbers) == 0:  # Base case
        return 0
    return numbers[0] + recursive_sum(numbers[1:])


def reverse_string(text):
    if len(text) <= 1:  # Base case
        return text
    return reverse_string(text[1:]) + text[0]

print("Factorial:", factorial(5))
print("List sum:", recursive_sum([]))
print("Reversed string:", reverse_string("dog dog dog"))
