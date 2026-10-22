from datetime import date

# year = int(input("Enter your birth year: "))
# month = int(input("Enter your birth month (1-12): "))
# day = int(input("Enter your birth day: "))
birth = date(2006, 1, 3)  
# birth = date(year, month, day)
today = date.today()

age = today.year - birth.year
if (today.month, today.day) < (birth.month, birth.day):
    age -= 1

next_birthday = date(today.year, birth.month, birth.day)

if next_birthday < today:
    next_birthday = date(today.year + 1, birth.month, birth.day)

days_left = (next_birthday - today).days

print("Your age is:", age, "years")
print("Days until next birthday:", days_left)
