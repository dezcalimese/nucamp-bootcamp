def show_balance(balance):
    print("Current balance: $", float(balance))


def deposit(balance):
    amount = input("Enter amount to deposit: ")
    amount_int = float(amount)
    return balance + amount_int


def withdraw(balance):
    amount = input("Enter amount to withdraw: ")
    amount_int = float(amount)
    return balance - amount_int


def logout(name):
    print("Goodbye " + name + "!")
