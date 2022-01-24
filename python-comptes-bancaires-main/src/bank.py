from customer import Customer
from account import Account


class Bank:
    def __init__(self, bank_name, customers):
        self.customers = [Customer]
        self.to_account = None
        self.from_account = None
        self.amount = None
        self.bank_name = bank_name

    def create_account(self):
        print("Enter your name : ")
        client_name = input()
        print("I truly hate python, anyway, Welcome in our bank, " + client_name)
        Customer.current_account = Account()

    def delete_account(self):
        print("Confirm that you want to delete your account : Y/N ")
        confirmation = input()
        if confirmation == "Y":
            Customer.current_account = None
        elif confirmation == "N":
            print("Ok keep your account")

    def new_customer(self):
        print(
            "1. Create an account\n"
            "0. Exit"
        )
        client_choice = str(input())
        if client_choice == "1":
            self.create_account()
        if client_choice == "0":
            print("I truly hate Git, Bye !")

    def transfert(self, amount, from_account, to_account):
        self.amount = amount
        self.from_account = from_account
        self.to_account = to_account

        if amount < 0:
            raise RuntimeError("Deposit negative")
