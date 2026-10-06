
squares = [number ** 2 for number in range(1, 11)]
print(squares)



numbers = [1, 2, 2, 3, 1, 4, 3, 5]

unique_numbers = {number for number in numbers}

print(unique_numbers)



even_numbers = [number for number in range(1, 11) if number % 2 == 0]

print(even_numbers)