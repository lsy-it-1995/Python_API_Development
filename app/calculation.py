def add(num1: int, num2: int):
    return num1 + num2

def mult(num1: int, num2: int):
    return num1 * num2;

def sub(num1: int, num2: int):
    return num1 - num2;

class Insufficient_fund(Exception):
    pass

class BankAccount():
    def __init__(self, starting_balance = 0):
        self.balance = starting_balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise Insufficient_fund("Insufficient funds in account")
        self.balance -= amount
    def collect_interest(self):
        self.balance *= 1.1
        