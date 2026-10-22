""" append dated entries to a text file and read them back"""
from datetime import datetime
while True:
    print("\n1. Add diary entry")
    print("2. Read diary entries")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        date = datetime.now().strftime("%Y-%m-%d")
        entry = input("Write your diary entry: ")

        with open("diary.txt", "a") as file:
            file.write(date + ": " + entry + "\n")

        print("Entry saved!")

    elif choice == "2":
        with open("diary.txt", "r") as file:
            for line in file:
                print(line.strip())

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
