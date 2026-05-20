FILE_NAME = "expenses.txt"


def save_expense(expense):

    with open(FILE_NAME, "a") as file:
        file.write(expense + "\n")


def read_expenses():

    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()

    except FileNotFoundError:
        return []