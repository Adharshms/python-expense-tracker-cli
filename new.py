import json
import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

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

def export_to_csv():
    expenses = load_expenses()
    if not expenses:
        print("⚠️ No expenses to export.")
        return
    with open("expenses.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category", "note", "date"])
        writer.writeheader()
        writer.writerows(expenses)
    print("✅ Exported to expenses.csv")

def show_pie_chart():
    expenses = load_expenses()
    if not expenses:
        print("⚠️ No expenses to display.")
        return
    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp["category"]] += exp["amount"]
    categories = list(category_totals.keys())
    amounts = list(category_totals.values())
    
    plt.figure(figsize=(6,6))
    plt.pie(amounts, labels=categories, autopct="%1.1f%%", startangle=90)
    plt.title("Expense Breakdown by Category")
    plt.tight_layout()
    plt.show()

def main():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Export to CSV\n4. Show Pie Chart\n5. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            export_to_csv()
        elif choice == "4":
            show_pie_chart()
        elif choice == "5":
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()
