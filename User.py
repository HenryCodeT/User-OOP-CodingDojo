class User:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.account_balance =  0 

    def make_deposit(self,amount):
        self.account_balance += amount
    def make_withdraw(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f'User: {self.firstname} {self.lastname}, Balance: ${self.account_balance}')
    def transfer_dinero(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()