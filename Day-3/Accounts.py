class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

    def withdrawal(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return (self.interestRate * self.balance) / 100

demo = SavingsAccount("Mark", 2000, 5)
print("Initial Balance:", demo.getBalance())
demo.withdrawal(1000)
print("Balance after withdrawal:", demo.getBalance())
demo.deposit(500)
print("Balance after deposit:", demo.getBalance())
print("Interest on current balance:", demo.interestAmount())
