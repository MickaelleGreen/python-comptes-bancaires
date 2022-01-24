class Customer:
    def __init__(self, name, bank, current_account, savings_account):
        self. name = name
        self.bank = bank
        self.current_account = current_account
        self.savings_account = savings_account

    def deposit_money(self, amount_money):
        if amount_money < 0:
            raise RuntimeError("Deposit negative !")

        self.current_account += amount_money
        print("You have now " + self.current_account + " on you account")




