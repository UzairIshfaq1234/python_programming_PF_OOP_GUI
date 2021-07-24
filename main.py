from current import Current
from saving import saving

class main:

    def __init__(self, owner):
        self.owner = owner

        self.accounts = []

    def add_account(self, account):
        
        self.accounts.append(account)

    def get_account(self, account_number):
        return self.accounts[account_number]

    def get_customer_info(self):
        print("_____________________________")
        print("NAME: ", self.owner)
        print("ACCOUNT:")
        for account in self.accounts:
            print(" Status: ", account.account_type)
            print(" balance: ", account.get_balance())

        print("________________________________")

