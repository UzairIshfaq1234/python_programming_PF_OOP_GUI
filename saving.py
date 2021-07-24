from bank import Bank

class saving(Bank):

    def __init__(self, balance):
        super().__init__(balance)
        self.account_status = "saving"

    def add_profit(self):
        year = super().get_year()
        year += 1
        super().set_year(year)

        balance = super().get_balance()
        balance += 500

        super().set_balance(balance)

    def withdraw_balance(self, balance):
        balance = super().get_balance()

        if super().get_year() == 1:
            balance -= 10
            print(" 10 rupees! deducted")
            super().set_balance(balance)

            return balance