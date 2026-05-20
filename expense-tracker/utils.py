def validate_amount(amount):

    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False