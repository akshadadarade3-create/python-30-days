marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)
total =sum(marks)
average = total/len(marks)
print("Sum:",sum(marks))
print("Average:",average)
print("Highest:",max(marks))
print("lowest:",min(marks))






