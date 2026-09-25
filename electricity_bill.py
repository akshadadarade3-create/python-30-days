"""Units consumed:Rate
First 100 units:₹5/unit
Next 100 units:₹7/unit
Next 100 units:₹10/unit
Above 300 units:₹12/unit"""

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
elif units <= 300:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)
else:
    bill = (100 * 5) + (100 * 7) + (100 * 10) + ((units - 300) * 12)
print("Electricity Bill: ₹", bill)