
import random
import string

passwords = {}

# read old passwords
try:
    with open("password_manager.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":", 1)
            passwords[website] = pwd
except FileNotFoundError:
    pass


def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    
    length = int(input("Enter password length: "))

    if length < 6:
        print("Password should be at least 6 characters.")
        return

    password = ""

    for i in range(length):
        password += random.choice(chars)

    print("Generated password:", password)


while True:

    print("\n_____ PASSWORD MANAGER _____")
    print("1. Save password")
    print("2. View password")
    print("3. Generate password")1
    print("4. Delete password")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        website = input("Enter website name: ")
        pwd = input("Enter password: ")

        if website in passwords:
            print("Password for this website already exists.")
        else:
            passwords[website] = pwd

            with open("password_manager.txt", "a") as file:
                file.write(f"{website}:{pwd}\n")

            print("Password saved successfully!")

    elif choice == "2":

        website = input("Enter website name: ")

        if website in passwords:
            print("Password:", passwords[website])
        else:
            print("No password found for this website.")

    elif choice == "3":

        try:
            generate_password()
        except ValueError:
            print("Please enter a number.")

    elif choice == "4":

        website = input("Enter website name: ")

        if website in passwords:
            del passwords[website]

            with open("password_manager.txt", "w") as file:
                for website, pwd in passwords.items():
                    file.write(f"{website}:{pwd}\n")

            print("Password deleted successfully!")
        else:
            print("No password found for this website.")

    elif choice == "5":
        print("Exiting password manager...")
        break

    else:
        print("Invalid choice. Please try again.")