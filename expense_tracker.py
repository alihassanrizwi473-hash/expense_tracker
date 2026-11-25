expenses = []
balance = 0


def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    print("\nCategories:")
    print("1. Food")
    print("2. Transport")
    print("3. Shopping")
    print("4. Bills")
    print("5. Education")

    choice = input("Enter category number: ")

    if choice == "1":
        category = "Food"
    elif choice == "2":
        category = "Transport"
    elif choice == "3":
        category = "Shopping"
    elif choice == "4":
        category = "Bills"
    elif choice == "5":
        category = "Education"
    else:
        print("Invalid category!")
        return

    expense = {
        "name": name,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    global balance
    balance = balance - amount

    with open("expenses.txt", "a") as file:
        file.write(
            f"Expense: {name} | Amount: {amount} | Category: {category}\n"
        )

    print("Expense added successfully!")


def show_expenses():
    if len(expenses) == 0:
        print("No expenses added yet.")
        return

    print("\n===== EXPENSE RECORD =====")

    for expense in expenses:
        print(
            "Name:", expense["name"],
            "| Amount:", expense["amount"],
            "| Category:", expense["category"]
        )


def total_expense():
    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense =", total)


def remaining_amount():
    print("Remaining Amount =", balance)


print("===== EXPENSE TRACKER =====")

balance = float(input("Enter your available amount: "))

while True:

    print("\n===== MENU =====")
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Total Expense")
    print("4. Remaining Amount")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        remaining_amount()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")