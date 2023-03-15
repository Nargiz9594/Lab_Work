#задание1
# BankAccount.py - Nargiz
class BankAccount:
    def __init__(self, balance: float | int, name: str, account_number):
        self.balance = balance
        self.name = name
        self.account_number = account_number

        # Задание 2
class BankAccount(object):

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount
    def overdrawn(self):
        return self.balance < 0


    #задание 3


def deposit(self, amount):
    self.balance += amount
    return self.balance

#задание 4

    def withdraw(self, amount):

        if amount > self.balance:
            raise RuntimeError
        self.balance -= amount
        return self.balance
    #задание 5

    def bank_fes(self,):
        self.balance += self.balance * 0.05
        return f 'баланс с  комиссией равен {self.balance}'

        #задание 6

def display(self):

    total = f'Account holder name {self.name}\n,' \
            f'Owner account number {self.account_number}\n,' \
            f'Balance {self.balance}'
    print(total)
    return total



