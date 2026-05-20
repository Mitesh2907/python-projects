from expense_manager import ExpenseManager

def show_menu():
    print("\n====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expense")
    print("4. Search Expense")
    print("5. Exit")


manager = ExpenseManager()

while True:
    show_menu()

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter expense title: ")
        amount = input("Enter amount: ")
        category = input("Enter category: ")

        manager.add_expense(title, amount, category)

    elif choice == "2":
        manager.view_expenses()

    elif choice == "3":
        manager.show_total_expense()

    elif choice == "4":
        keyword = input("Enter keyword to search: ")
        manager.search_expense(keyword)

    elif choice == "5":
        print("Exiting Expense Tracker...")
        break

    else:
        print("Invalid choice.")