def read_file():
    filename = input("Enter the file name to read: ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'.")
    else:
        print(content)
    finally:
        print("File reading attempt finished.")
read_file()
