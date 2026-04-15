class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    # deposit
    def deposit(self, amount):
        self.balance += amount
        return self

    # withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    # display account info
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # yield interest
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


# create 2 accounts
account1 = BankAccount(0.02, 0)
account2 = BankAccount(0.03, 0)


# account1: 3 deposits + 1 withdrawal + interest + display (chaining)
account1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()


# account2: 2 deposits + 4 withdrawals + interest + display (chaining)
account2.deposit(500).deposit(200).withdraw(100).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()