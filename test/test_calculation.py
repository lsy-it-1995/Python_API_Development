import pytest
from app.calculation import BankAccount, add, sub, mult, Insufficient_fund

@pytest.fixture
def zero_bank_account():
    print("bank create")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 4, 7),
    (1, 2, 3),
    (10,1, 11)
])
def test_add(num1, num2, expected):
    assert add(num1, num2) == expected

def test_sub():
    assert sub(-3,2) == -5

def test_mult():
    assert mult(2,0) == 0

def test_bank_set_initial_amount(zero_bank_account):
    # assert zero_bank_account.balance == 1
    pass

def test_bank_default_amount(bank_account):
    assert bank_account.balance == 50

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55

@pytest.mark.parametrize("deposited, withdraw, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(deposited, withdraw, expected, zero_bank_account):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdraw)
    assert zero_bank_account.balance == expected

def test_insufficient_funds(bank_account):
    with pytest.raises(Insufficient_fund):
        bank_account.withdraw(200)
