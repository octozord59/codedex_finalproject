# #04 of Classes and Objects

class BankAccount():
    def __init__(self, first_name, last_name, account_id, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.pin = pin
        self.balance = balance

    def deposit(self, add_money):
        print('You have deposited ' + str(add_money) + ' and your new balance is:  ' + str(int(self.balance) + add_money))

    def withdraw(self, rem_money):
        print('You have withdrawn ' + str(rem_money) + ' dollars and your new balance is:' + str(self.balance - rem_money))

    def current_balance(self):
        print('Your balance is:  ' + str(self.balance))

adeel = BankAccount('Adeel', 'Ahmed', '1011251', '0905', 10)

print(vars(adeel))

adeel.deposit(90)
adeel.withdraw(20)
adeel.current_balance()