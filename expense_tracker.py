# Personal Expense Tracker
# Simple console program to keep track of daily spending.
# Data is saved in a file called expenses.json so nothing is lost
# when you close the program.

import csv
import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    # if the file is not there yet, just start with an empty list
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
        return data
    except:
        # file is empty or broken, start fresh
        print("Could not read old data, starting with an empty list.")
        return []


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def get_amount():
    # keep asking until the user types a proper positive number
    while True:
        amount = input("Amount (Rs): ")
        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount should be more than 0. Try again.")
            else:
                return amount
        except ValueError:
            print("That is not a number. Try again.")


def get_date():
    # user can just press enter to use today's date
    while True:
        date_text = input("Date (YYYY-MM-DD) or press Enter for today: ")

        if date_text == "":
            return datetime.now().strftime("%Y-%m-%d")

        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return date_text
        except ValueError:
            print("Wrong date format. Example: 2026-10-22")


def add_expense(expenses):
    print("\n--- Add New Expense ---")

    title = input("What did you spend on? ").strip()
    if title == "":
        print("Title cannot be empty.")
        return

    amount = get_amount()
    category = input("Category (food, travel, bills, shopping...): ").strip().lower()
    if category == "":
        category = "other"

    date = get_date()

    expense = {
        "title": title,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added!")


def show_expenses(expenses):
    print("\n--- All Expenses ---")

    if len(expenses) == 0:
        print("No expenses yet.")
        return

    print("No.  Date         Category      Amount     Title")
    print("-" * 55)

    number = 1
    for e in expenses:
        print(f"{number:<4} {e['date']:<12} {e['category']:<13} {e['amount']:<10.2f} {e['title']}")
        number = number + 1


def delete_expense(expenses):
    show_expenses(expenses)

    if len(expenses) == 0:
        return

    choice = input("\nEnter the number of the expense to delete (or press Enter to cancel): ")

    if choice == "":
        return

    if not choice.isdigit():
        print("Please type a number.")
        return

    index = int(choice) - 1

    if index < 0 or index >= len(expenses):
        print("No expense with that number.")
        return

    removed = expenses.pop(index)
    save_expenses(expenses)
    print("Deleted:", removed["title"])


def show_total(expenses):
    total = 0
    for e in expenses:
        total = total + e["amount"]

    print("\nTotal spent so far: Rs", round(total, 2))


def category_summary(expenses):
    print("\n--- Spending by Category ---")

    if len(expenses) == 0:
        print("No expenses yet.")
        return

    totals = {}
    for e in expenses:
        cat = e["category"]
        if cat in totals:
            totals[cat] = totals[cat] + e["amount"]
        else:
            totals[cat] = e["amount"]

    grand_total = sum(totals.values())

    for cat in totals:
        percent = (totals[cat] / grand_total) * 100
        print(f"{cat:<15} Rs {totals[cat]:<10.2f} ({percent:.1f}%)")

    print("-" * 40)
    print(f"{'Total':<15} Rs {grand_total:.2f}")


def monthly_summary(expenses):
    print("\n--- Monthly Summary ---")

    month = input("Enter month (YYYY-MM), e.g. 2026-10: ").strip()

    month_total = 0
    count = 0

    for e in expenses:
        # date looks like 2026-10-22, so first 7 letters are the month
        if e["date"][:7] == month:
            month_total = month_total + e["amount"]
            count = count + 1
            print(f"{e['date']}  {e['category']:<12} Rs {e['amount']:.2f}  {e['title']}")

    if count == 0:
        print("No expenses found for that month.")
    else:
        print(f"\n{count} expenses, total Rs {month_total:.2f}")


def export_to_csv(expenses):
    print("\n--- Save as CSV ---")

    if len(expenses) == 0:
        print("Nothing to save, add some expenses first.")
        return

    name = input("File name (press Enter for expenses.csv): ").strip()
    if name == "":
        name = "expenses.csv"

    # add .csv at the end if the user forgot
    if not name.endswith(".csv"):
        name = name + ".csv"

    try:
        with open(name, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Amount", "Title"])

            for e in expenses:
                writer.writerow([e["date"], e["category"], e["amount"], e["title"]])

        print("Saved", len(expenses), "expenses to", name)
        print("You can open it in Excel or Google Sheets.")
    except PermissionError:
        print("Could not save the file. Close it if it is open in Excel and try again.")


def show_menu():
    print("\n==============================")
    print("   PERSONAL EXPENSE TRACKER")
    print("==============================")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. Delete an expense")
    print("4. Show total spent")
    print("5. Spending by category")
    print("6. Monthly summary")
    print("7. Save as CSV")
    print("8. Exit")


def main():
    expenses = load_expenses()

    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_expenses(expenses)
        elif choice == "3":
            delete_expense(expenses)
        elif choice == "4":
            show_total(expenses)
        elif choice == "5":
            category_summary(expenses)
        elif choice == "6":
            monthly_summary(expenses)
        elif choice == "7":
            export_to_csv(expenses)
        elif choice == "8":
            print("Bye! Keep saving :)")
            break
        else:
            print("Invalid option, please pick between 1 and 8.")


main()
