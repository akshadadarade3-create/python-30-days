numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second_largest = float('-inf')

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number
print("numbers:", numbers)
print("Largest:", largest)
print("Second largest:", second_largest)