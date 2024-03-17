"""
Create Account class with 2 attribute -balance and account no.

Create methods to debit,credit, and printing the balance.
"""
class Account:
    def __init__ (self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance-=amount
        print("Debited amount: ",amount)
        print("Total Balance After Debit: ",self.balance)
    def credit(self,amount):
        self.balance+=amount
        print("Credited amount: ",amount)
        print("Total Balance After Credit: ",self.balance)
    def print_balance(self):
            print("Current Balance: ",self.balance)

my_bank_account=Account(1000,123456789)
my_bank_account.debit(200)
my_bank_account.credit(300)
my_bank_account.print_balance()