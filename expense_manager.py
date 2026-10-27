from datetime import datetime
import math
from storage import save_expenses

def get_next_id(expenses):
    return max((expense.get("id", 0) for expense in expenses),default=0 ) + 1

def add_expense(expenses, amount, category, description, date):
    """Validate and add a new expense."""
    try:
        amount = float(amount)
        if not math.isfinite(amount) or amount <= 0:
            print("Amount must be a positive number.")
            return False
    except (ValueError, TypeError):
        print("Invalid amount. Enter a valid number.")
        return False
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        print("Invalid date. Use YYYY-MM-DD format.")
        return False

    if not category.strip() or not description.strip():
        print("Category and description cannot be empty.")
        return False

    expense = {
        "id": get_next_id(expenses),
        "amount": round(amount, 2),
        "category": category.strip(),
        "description": description.strip(),
        "date": date.isoformat()
    }
    expenses.append(expense)
    if save_expenses(expenses):
        print("Expense added successfully!")
        return True
    expenses.pop()
    return False

def view_expenses(expenses):
    """Display expenses in a table."""
    if not expenses:
        print("No expenses found.")
        return
    print("*" * 85)
    print(f"{'ID':<5}{'Date':<13}{'Category':<26}{'Description':<30}{'Amount':>12}")
    print("*" * 85)

    for expense in sorted(expenses, key=lambda item: (item["date"], item["id"])):
        print( f"{expense['id']:<5}{expense['date']:<13}{expense['category']:<17}{expense['description'][:28]:<30}{expense['amount']:>12.2f}")
    print("-" * 85)
    print(f"Grand Total: {sum(e['amount'] for e in expenses):.2f}")

def show_category_totals(expenses):
    """Calculate and display totals for each category."""
    if not expenses:
        print("No expenses available.")
        return
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + expense["amount"]

    print("\nTotals by Category")
    for category, total in sorted(totals.items()):
        print(f"{category:<20} {total:.2f}")

    print(f"{'Grand Total':<20} {sum(totals.values()):.2f}")

def filter_by_month(expenses, month):
    """Filter expenses by YYYY-MM."""
    try:
        datetime.strptime(month, "%Y-%m")
    except (ValueError, TypeError):
        print("Invalid month. Use YYYY-MM, for example 2026-10.")
        return

    filtered = [expense for expense in expenses
        if expense["date"].startswith(month)]
    print(f"\nExpenses for {month}")
    view_expenses(filtered)

def delete_expense(expenses, expense_id):
    """Delete an expense using its ID."""
    try:
        expense_id = int(expense_id)
    except (ValueError, TypeError):
        print("Please enter a valid numeric ID.")
        return

    for index, expense in enumerate(expenses):
        if expense["id"] == expense_id:
            removed = expenses.pop(index)

            if save_expenses(expenses):
                print(f"Deleted expense: {removed['description']}")
            else:
                expenses.insert(index, removed)
            return
    print("Expense ID not found.")
