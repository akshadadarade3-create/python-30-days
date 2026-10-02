data = input("Enter Data:")
frequency = {}

for char in data:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

for char, count in frequency.items():
    print(char, ":", count)