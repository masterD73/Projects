# Reviewer: Alexander.
from pytest import fixture

DEPOSIT = 666
WITHDRAWAL = 50
TEST_ID = 5512435


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


@fixture()
def set_up():
    return BankAccount(TEST_ID)


def test_get_id(set_up):
    assert set_up.customer_id == TEST_ID


def test_account_empty(set_up):
    assert set_up.balance == 0


def test_account_withdrawal_empty(set_up):
    set_up.withdrawal(WITHDRAWAL)
    assert set_up.balance == 0


def test_account_deposit(set_up):
    set_up.deposit(DEPOSIT)
    assert set_up.balance == DEPOSIT


def test_account_deposit_withdrawal(set_up):
    set_up.deposit(DEPOSIT)
    set_up.withdrawal(WITHDRAWAL)
    assert set_up.balance == DEPOSIT - WITHDRAWAL


def test_account_negative_deposit(set_up):
    set_up.deposit(-DEPOSIT)
    assert set_up.balance == -DEPOSIT


def test_account_negative_withdrawal(set_up):
    set_up.withdrawal(-WITHDRAWAL)
    assert set_up.balance == WITHDRAWAL
