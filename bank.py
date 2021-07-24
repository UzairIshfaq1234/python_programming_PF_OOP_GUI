class Bank:

    def __init__(self, balance):
        self.balance = balance
        self.accounts = []

        self.year = 1

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    def deposit(self, balance):
        self.balance += balance

    def withdraw(self, deduct):
        self.balance -= deduct

        return self.balance

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year
