# Reviewer: Alexander.
import unittest


class BankAccount:
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.balance = 0

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True


class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.deposit = 666
        self.withdrawal = 50
        self.test_id = 5512435
        self.account = BankAccount(self.test_id)

    def tearDown(self):
        del self

    def test_get_id(self):
        self.assertEqual(self.account.customer_id, self.test_id)

    def test_account_empty(self):
        self.assertEqual(self.account.balance, 0)

    def test_account_withdrawal_empty(self):
        self.account.withdrawal(self.deposit)
        self.assertEqual(self.account.balance, 0)

    def test_account_Deposit(self):
        self.account.deposit(self.deposit)
        self.assertEqual(self.account.balance, self.deposit)

    def test_account_deposit_withdrawal(self):
        self.account.deposit(self.deposit)
        self.account.withdrawal(self.withdrawal)
        self.assertEqual(self.account.balance, self.deposit - self.withdrawal)

