"""a function that accepts any number of values and returns their average"""
def average(*args):
    if len(args) == 0:
        raise ValueError("at least one value is required")
    total = sum(args)
    return total / len(args)
print(average(50,57,61))
print(average(70,80,90,75))


