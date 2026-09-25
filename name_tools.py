name = input("Enter Your Full Name :")
print(name.upper())
print(name.lower())
print(name[::-1])
print(name.title())
words = name.split()
initials = words[0][0] + " " + words[1][0] + " " + words[2][0]

print("Initials:", initials)