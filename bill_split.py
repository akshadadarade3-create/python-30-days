Bill = int(input("Enter Total Bill:"))
Tip_Percentage = int(input("Enter Tip Percentage:"))
people = int(input("Enter Total Number of People:"))
Tip = (Bill*Tip_Percentage)/100
total = Bill + Tip
share = total/people
print("Bill",Bill)
print("Tip",Tip)
print("people",people)
print("Each Person Pays",share)