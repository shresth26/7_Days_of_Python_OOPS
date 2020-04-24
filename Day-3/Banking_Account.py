class Account:
    def __init__(self, title = None, balance = 0):
        self.title = title
        self.balance = balance

    def printDetails(self):
        print("Welcome Mr.", self.title, "your account balance is", self.balance)

class SavingsAccount(Account):

    def __init__(self, title = None, balance = 0, interestRate = 0):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def printAccDetails(self):
        self.printDetails()
        print("And the interest rate is", self.interestRate, "percent.")


save = SavingsAccount("Mark", 5000, 5)
save.printAccDetails()
