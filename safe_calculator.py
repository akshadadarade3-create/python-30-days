def calculator():
    while True:
        try:
            first = input("\nEnter the first number (or exit to quit the Program): ").strip()
            if first.lower() == "exit":
                print("Calculator closed.")
                break
            second = input("Enter the second number: ").strip()
            operation = input("Choose operation (+, -, *, /): ").strip()

            num1 = float(first)
            num2 = float(second)

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError(
                        "Cannot divide by zero."
                    )
                result = num1 / num2
            else:
                raise ValueError("Use +, -, *, /.")

        except ValueError as error:
            print("Input error:", error)
        except ZeroDivisionError as error:
            print("Math error:", error)
        else:
            print("Result:", result)
        finally:
            print("program finised successfullly.")
calculator()
