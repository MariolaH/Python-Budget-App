class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        # check to see if have right amount of funds
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
        else:
            return False
    
    def get_balance(self):
        for amount in self.ledger:
            self.balance += amount

# transfer from 1 category to another
    def transfer(self,amount, category):
        if (self.check_funds(amount)):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from" + self.name)
            return True
        else:
            return False

 
    def check_funds(self, amount):
        if amount < self.balance:
            return False
        else:
            return True    

# print ((__str__)


