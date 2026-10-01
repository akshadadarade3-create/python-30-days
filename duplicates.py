numbers = [1, 2, 2, 3, 1, 4, 3, 5,288,288,4,8]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print("Original list:", numbers)
print("Without duplicates:", unique_numbers)
