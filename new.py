import json
from datetime import datetime

FILE = "expenses.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (food, travel, etc): ")
    note = input("Enter a note: ")
    date = datetime.now().strftime("%Y-%m-%d")
    expense = {"amount": amount, "category": category, "note": note, "date": date}
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added.")

def view_expenses():
    expenses = load_expenses()
    total = 0
    print("\nYour Expenses:")
    for exp in expenses:
        print(f"₹{exp['amount']} - {exp['category']} ({exp['note']}) on {exp['date']}")
        total += exp['amount']
    print(f"\n💰 Total Spent: ₹{total}")

def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
