import getpass
from datetime import datetime

balance = 10000
correct_pin = "1234"
attempts = 3
transactions = []


def log_transaction(text):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    transactions.append(time_now + " - " + text)


def check_balance():
    print("your current balance is:", balance)


def withdraw_money():
    global balance
    try:
        amount = float(input("enter amount to withdraw: "))
    except ValueError:
        print("that's not a valid number")
        return

    if amount <= 0:
        print("amount should be more than 0")
    elif amount % 100 != 0:
        print("amount should be in multiples of 100")
    elif amount > balance:
        print("insufficient balance")
    else:
        balance -= amount
        log_transaction("withdraw " + str(amount))
        print("please collect your cash")
        print("your new balance is", balance)


def deposit_money():
    global balance
    try:
        amount = float(input("enter amount to deposit: "))
    except ValueError:
        print("that's not a valid number")
        return

    if amount <= 0:
        print("amount should be more than 0")
    else:
        balance += amount
        log_transaction("deposit " + str(amount))
        print("deposit successful, new balance is", balance)


def mini_statement():
    print("\nlast few transactions:")
    if len(transactions) == 0:
        print("no transactions yet")
    else:
        for t in transactions[-5:]:
            print(t)


def change_pin():
    global correct_pin
    old_pin = getpass.getpass("enter current pin: ")
    if old_pin != correct_pin:
        print("wrong pin, cant change")
        return
    new_pin = getpass.getpass("enter new pin: ")
    confirm = getpass.getpass("confirm new pin: ")
    if new_pin != confirm:
        print("pins didnt match")
    elif len(new_pin) != 4 or not new_pin.isdigit():
        print("pin has to be 4 digits")
    else:
        correct_pin = new_pin
        print("pin changed")


def login():
    tries = attempts
    while tries > 0:
        pin = getpass.getpass("enter your 4 digit pin: ")
        if pin == correct_pin:
            print("login successful\n")
            return True
        tries -= 1
        if tries > 0:
            print("wrong pin,", tries, "tries left")
        else:
            print("too many wrong attempts, card blocked")
    return False


print("---------- ATM ----------")

if login():
    while True:
        print("\n1. check balance")
        print("2. withdraw money")
        print("3. deposit money")
        print("4. mini statement")
        print("5. change pin")
        print("6. exit")

        option = input("enter your option: ")

        if option == "1":
            check_balance()
        elif option == "2":
            withdraw_money()
        elif option == "3":
            deposit_money()
        elif option == "4":
            mini_statement()
        elif option == "5":
            change_pin()
        elif option == "6":
            print("thank you for using the ATM")
            break
        else:
            print("invalid option, try again")