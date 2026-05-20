def is_valid_length(length):

    if not length.isdigit():
        return False

    length = int(length)

    if length < 4 or length > 50:
        return False

    return True