import json
data = [
    {
        "name": "Akshuu",
        "age": 25,
        "city": "Nashik"
    },
    {
        "name": "xyzzz",
        "age": 29,
        "city": "yyy"
    }
]
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    data = json.load(file)

print(data)
print(data[0]["name"]) 
print(data[1]["name"]) 
