from generator import generate_password
from validator import is_valid_length


def menu():
    print("\n====== Password Generator ======")
    print("1. Generate Password")
    print("2. Exit")


while True:

    menu()

    choice = input("Enter your choice: ")

    if choice == "1":

        length = input("Enter password length: ")

        if not is_valid_length(length):
            print("Please enter a valid number between 4 and 50.")
            continue

        use_digits = input("Include numbers? (yes/no): ").lower()
        use_symbols = input("Include symbols? (yes/no): ").lower()

        password = generate_password(
            int(length),
            use_digits,
            use_symbols
        )

        print(f"\nGenerated Password: {password}")

        save = input("Save password to file? (yes/no): ").lower()

        if save == "yes":

            with open("saved_passwords.txt", "a") as file:
                file.write(password + "\n")

            print("Password saved successfully.")

    elif choice == "2":
        print("Exiting Password Generator...")
        break

    else:
        print("Invalid choice.")