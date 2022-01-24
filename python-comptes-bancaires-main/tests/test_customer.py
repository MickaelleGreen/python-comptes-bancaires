from unittest import TestCase
from ./src import bank
from ./src import customer


class TestCustomer(TestCase):

    # test to check bank name of the client
    def test_bankName(self, bank_name):
        self.bank = bank_name

    # test to add account
    def test_adding_account(self, null=None):
        if customer.current_account != null:
            self.assertIsNotNone("You already have an account")

        elif customer.current_account == null:
            self.run(bank.create_account)


    # test to remove account
    def test_delete_account(self, null=None):
        if customer.current_account != null:
            self.run(bank.delete_account)