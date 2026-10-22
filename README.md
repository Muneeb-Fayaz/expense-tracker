# 💰 Personal Expense Tracker

A simple, beginner-friendly **Python console app** to keep track of your daily spending. No extra libraries, no setup headaches, just run it and start tracking.

---

## ✨ Features

- ➕ **Add expenses** with title, amount, category and date
- 📋 **View all expenses** in a neat table
- 🗑️ **Delete** any expense you added by mistake
- 🧮 **Total spent** so far, in one click
- 📊 **Category summary** with percentages (food, travel, bills...)
- 📅 **Monthly summary** to see where your money went in a given month
- 💾 **Auto-save** to a local file, so your data is safe after closing the program
- 🛡️ **Input checks** for wrong amounts and wrong date formats

---

## 🚀 Getting Started

### Requirements

- Python 3.6 or higher
- That's it! Only built-in modules are used (`json`, `os`, `datetime`)

### Run the program

```bash
python expense_tracker.py
```

---

## 🖥️ How It Looks

```
==============================
   PERSONAL EXPENSE TRACKER
==============================
1. Add expense
2. View all expenses
3. Delete an expense
4. Show total spent
5. Spending by category
6. Monthly summary
7. Exit
Choose an option (1-7):
```

### Example: Viewing expenses

```
No.  Date         Category      Amount     Title
-------------------------------------------------------
1    2026-10-20   food          250.00     Lunch with friends
2    2026-10-21   travel        120.00     Auto fare
3    2026-10-22   bills         899.00     Internet recharge
```

### Example: Category summary

```
food            Rs 250.00     (19.7%)
travel          Rs 120.00     (9.5%)
bills           Rs 899.00     (70.8%)
----------------------------------------
Total           Rs 1269.00
```

---

## 📖 How to Use

1. **Add an expense**: choose option `1`, then enter what you spent on, the amount, a category, and the date. Press **Enter** on the date to use today's date.
2. **Check your spending**: use options `2`, `4`, `5` or `6` to see your list, total, category split, or a particular month.
3. **Fix a mistake**: choose option `3`, pick the number of the expense, and it's removed.
4. **Exit** with option `7`. Your data is already saved.

---

## 📁 Project Structure

```
expense-tracker/
│
├── expense_tracker.py   # main program
├── expenses.json        # created automatically when you add your first expense
└── README.md            # you are here
```

---

## 🗂️ How Data Is Stored

Expenses are saved in `expenses.json` in this format:

```json
[
    {
        "title": "Lunch with friends",
        "amount": 250.0,
        "category": "food",
        "date": "2026-10-20"
    }
]
```

You can open this file in any text editor, but it's best to let the program manage it.

---

## 🔮 Ideas for Future Improvements

- [ ] Monthly budget limit with a warning
- [ ] Export expenses to a CSV / Excel file
- [ ] Edit an existing expense
- [ ] Search by category or date range
- [ ] Simple charts using `matplotlib`

---

## 🤝 Contributing

Feel free to fork this project, play around with the code and add your own features. It's written in plain, simple Python so it's easy to understand and modify.

---

## 📝 License

Free to use for learning and personal projects.

---

⭐ *Track small, save big. Happy saving!*
