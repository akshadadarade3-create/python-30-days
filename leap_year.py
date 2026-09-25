year = int(input("Enter Year:"))
if year%400 ==0 :
    print("Leap Year")
elif year %4 == 0 and year % 100 != 0:
    print("leap Year")
else :
    print("Not A Leap Year")