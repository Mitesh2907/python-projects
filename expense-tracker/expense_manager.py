from file_handler import save_expense, read_expenses
from utils import validate_amount


class ExpenseManager:

    def add_expense(self, title, amount, category):

        if not validate_amount(amount):
            print("Invalid amount.")
            return

        expense_data = f"{title},{amount},{category}"

        save_expense(expense_data)

        print("Expense added successfully.")

    def view_expenses(self):

        expenses = read_expenses()

        if len(expenses) == 0:
            print("No expenses found.")
            return

        print("\n------ Expense List ------")

        for index, expense in enumerate(expenses, start=1):

            data = expense.strip().split(",")

            if len(data) == 3:
                title, amount, category = data

                print(f"{index}. {title}")
                print(f"   Amount   : ₹{amount}")
                print(f"   Category : {category}")
                print()

    def show_total_expense(self):

        expenses = read_expenses()

        total = 0

        for expense in expenses:

            data = expense.strip().split(",")

            if len(data) == 3:
                total += float(data[1])

        print(f"\nTotal Expense: ₹{total}")

    def search_expense(self, keyword):

        expenses = read_expenses()

        found = False

        print("\n------ Search Result ------")

        for expense in expenses:

            if keyword.lower() in expense.lower():

                data = expense.strip().split(",")

                if len(data) == 3:
                    title, amount, category = data

                    print(f"Title    : {title}")
                    print(f"Amount   : ₹{amount}")
                    print(f"Category : {category}")
                    print()

                    found = True

        if not found:
            print("No matching expense found.")