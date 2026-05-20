import random
import string


def generate_password(length, use_digits, use_symbols):

    characters = string.ascii_letters

    if use_digits == "yes":
        characters += string.digits

    if use_symbols == "yes":
        characters += "!@#$%^&*()_+-="

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password