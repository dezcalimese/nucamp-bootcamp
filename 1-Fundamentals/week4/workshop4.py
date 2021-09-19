class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def transfer_money(self, name, amount):
        print("You are transferring $" + str(amount), "to", bankuser1.name)
        print("Authentication required")
        pin = int(input("Enter your PIN: "))
        if pin == bankuser1.pin:
            print("Transfer authorized")
            print("Transferring $" + str(amount) + " to", bankuser1.name)
            bankuser2.withdraw(amount)
            bankuser1.deposit(amount)
        else:
            print("Invalid PIN. Transaction canceled.")

    def request_money(self, name, amount):
        print("\nYou are requesting $" + str(amount), "from", name)
        print("User authentication is required...")
        pin = int(input("Enter " + bankuser1.name + "'s PIN: "))
        if pin == bankuser1.pin:
            password = input("Enter your password: ")
            if password == bankuser2.password:
                print("Request authorized")
                bankuser1.withdraw(amount)
                bankuser2.deposit(amount)
            elif password != bankuser2.password:
                print("Invalid password. Transaction canceled.")
        else:
            print("Invalid PIN. Transaction canceled.")
        bankuser2.show_balance()
        bankuser1.show_balance()


""" Driver Code for Task 1 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)


""" Driver Code for Task 2 """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)

""" Driver Code for Task 3 """
# bankuser1 = BankUser("Bob", 1234, "password")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)

""" Driver Code for Task 4 """
# bankuser1 = BankUser("Bob", 1234, "password")
# bankuser1.show_balance()
# bankuser1.deposit(5000.0)
# bankuser1.show_balance()
# bankuser1.withdraw(4000.0)
# bankuser1.show_balance()

""" Driver Code for Task 5 """
bankuser1 = BankUser("Bob", 1234, "password")
bankuser2 = BankUser("Alice", 4321, "coolerpassword")
bankuser2.deposit(5000.0)
bankuser2.show_balance()
bankuser1.show_balance()
print("")
bankuser2.transfer_money(bankuser1.name, 400)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser2.request_money(bankuser1.name, 250)
