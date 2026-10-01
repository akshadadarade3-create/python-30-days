shopping_list = ["clothes","grocery","cosmetics","medicines"]

while True:
    print("\n----- Shopping List -----")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(item, "added.")

    elif choice == "2":
        item = input("Enter item to remove: ")

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed.")
        else:
            print("Item not found.")

    elif choice == "3":
        print("\nShopping List:")

        if len(shopping_list) == 0:
            print("Your list is empty.")
        else:
            for item in shopping_list:
                print("-", item)

    elif choice == "4":
        print("bye")
        break

    else:
        print("Invalid choice.")