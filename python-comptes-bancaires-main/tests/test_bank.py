from unittest import TestCase
import pytest
from src.bank import Bank


class TestBank(TestCase):
    def test_transfert(self):
        '''Test BANK Transfert method'''
        self.account = Bank(50)
        self.account.deposit(50)

        self.assertEqual(self.account.balance, 55)

