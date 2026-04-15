class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    # deposit
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # withdrawal
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    # display balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    # BONUS: transfer money
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


# create 3 users
user1 = User("Ali", "ali@mail.com")
user2 = User("Sara", "sara@mail.com")
user3 = User("Omar", "omar@mail.com")


# user1
user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


# user2
user2.make_deposit(200).make_deposit(100).make_withdrawal(50).make_withdrawal(25).display_user_balance()


# user3
user3.make_deposit(300).make_withdrawal(50).make_withdrawal(50).make_withdrawal(50).display_user_balance()


# BONUS
user1.transfer_money(user3, 50).display_user_balance()
user3.display_user_balance()