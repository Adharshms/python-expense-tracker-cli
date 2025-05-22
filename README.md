 
 
💸 Python CLI Expense Tracker

A beginner-friendly command-line app to **track your personal expenses**, export them as CSV, and view category-wise spending with a pie chart — all in  pure Python!

---

🚀 Features

- ✅ Add expenses with amount, category & note
- 📂 Saves data locally in `expenses.json`
- 📊 View all your past expenses in a list
- 📤 Export expenses to CSV (`expenses.csv`)
- 🥧 View pie chart of spending by category (`matplotlib`)
- 🧠 Clean structure, beginner-friendly

---

🛠️ How to Run

1. Clone or download the repo
```bash
git clone https://github.com/yourusername/expense-tracker-cli.git
cd expense-tracker-cli
````

2. Install the required library

```bash
pip install matplotlib
```

3. Run the app

```bash
python expense_tracker.py
```

---

 🧪 Sample Usage

```text
1. Add Expense
2. View Expenses
3. Export to CSV
4. Show Pie Chart
5. Exit
Choose an option: 1
Enter amount: ₹150
Enter category: Food
Enter a note: Lunch at cafe
✅ Expense added.
```

---

📊 Pie Chart Output

When you choose option 4, a pie chart appears showing how you’ve spent across categories like food, travel, bills, etc.

---

📁 Project Structure

```
expense_tracker.py       # Main program
expenses.json            # Expense data (auto-created)
expenses.csv             # CSV export (optional)
README.md                # You're here!
```

---

🧠 Skills Demonstrated

* File handling (JSON & CSV)
* Python functions & CLI apps
* Simple data analysis
* Data visualization with `matplotlib`
* Beginner-level project structure
 

 🔮 Future Improvements (If given more time)
- Add login/signup for multi-user support
- Switch from JSON to SQLite database
- Add a simple Tkinter GUI or web dashboard

