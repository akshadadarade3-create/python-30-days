import json
import csv
import os
DATA_FILE = "expenses.json"
def load_expenses():
    """Load expenses from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            expenses = json.load(file)
        if isinstance(expenses, list):
            return expenses
        print("Error: Expense file has an invalid format.")
        return []
    except (json.JSONDecodeError, OSError):
        print("Could not read expenses.json. Starting with an empty list.")
        return []
    
def save_expenses(expenses):
    """Save expenses to the JSON file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)
        return True
    except OSError as error:
        print(f"Could not save expenses: {error}")
        return False

def export_csv(expenses, filename):
    """Export expenses to a CSV report."""
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "amount", "category", "description", "date"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(expenses)
        return True
    except (OSError, csv.Error) as error:
        print(f"Could not export CSV: {error}")
        return False
