"""a list of 8 product dictionaries (name, price, category, stock): print them as a table, filter by 
category, sort by price, list out-of-stock items, and calculate total inventory value """

products = [
    {"name": "Laptop", "price": 55000, "category": "Electronics", "stock": 10},
    {"name": "Mouse", "price": 800, "category": "Electronics", "stock": 25},
    {"name": "Keyboard", "price": 1500, "category": "Electronics", "stock": 15},
    {"name": "T-Shirt", "price": 700, "category": "Clothing", "stock": 20},
    {"name": "Jeans", "price": 1800, "category": "Clothing", "stock": 0},
    {"name": "Notebook", "price": 100, "category": "Stationery", "stock": 50},
    {"name": "Pen", "price": 20, "category": "Stationery", "stock": 100},
    {"name": "Headphones", "price": 2500, "category": "Electronics", "stock": 0}
]
print("Product List")

print(f"{'Name':<15}{'Price':<10}{'Category':<15}{'Stock':<10}")
print("-" * 50)

for product in products:
    print(
        f"{product['name']:<15}"
        f"{product['price']:<10}"
        f"{product['category']:<15}"
        f"{product['stock']:<10}"
    )

category = input("\nEnter category to filter: ")

filtered_products = [
    product
    for product in products
    if product["category"].lower() == category.lower()
]

print("Filtered list:", filtered_products)

print("\nFiltered Products")

for product in filtered_products:
    print(
        product["name"],
        "- ₹", product["price"],
        "- Stock:", product["stock"]
    )

sorted_products = sorted(
    products,
    key=lambda product: product["price"]
)

print("\nProducts Sorted by Price")

for product in sorted_products:
    print(product["name"], "- ₹", product["price"])


print("\nOut of Stock Products")
for product in products:
    if product["stock"] == 0:
        print(product["name"])

total_value = 0

for product in products:
    total_value += product["price"] * product["stock"]

print("\nTotal Inventory Value:", total_value)


print("\nFiltered Products")

for product in filtered_products:
    print(
        product["name"],
        "- ₹", product["price"],
        "- Stock:", product["stock"]
    )