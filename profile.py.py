"""a function that takes **kwargs and prints a formatted profile """
def profile(**kwargs):
    print("----- USER PROFILE -----")

    for key, value in kwargs.items():
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key}: {value}")

profile(
    your_name ="Akshuu",
    age = 2,
    city = "Pune",
    course = "Python Programming"
)
