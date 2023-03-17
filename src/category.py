class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.description = ""


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        print(f'{self.balance}.00 has been deposited into {self.name}')
        print(self.ledger)

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
            self.deposit(amount, "Transfer from" + self.name)
            return True
        else:
            return False
 
    def check_funds(self, amount):
        if amount < self.balance:
            print("Save to deposit")
            return True
        else:
            print("Insufficiant funds")
            return False   


    def __str__(self):
        print(f'**********{name}********')
        # print({self.ledger} + {self.balance})
        # print({self.balance})


# CATERGORIES (name)
initial_deposit = Category('Intial Deposit')
food = Category('food')
clothing = Category('clothing')
entertainment = Category('entertainment')

# deposit

initial_deposit.deposit(1000, 'deposit')

# withdraw

initial_deposit.withdraw(10.15, 'food')
initial_deposit.withdraw(50.00, 'clothing')
initial_deposit.withdraw(15.89, 'entertainment')
initial_deposit.withdraw(75, 'food')

# transfer

initial_deposit.transfer(75, clothing)


