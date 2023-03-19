class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0


    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        # print(f'{self.balance}.00 has been deposited into {self.name}')
        # print(self.ledger)

    def withdraw(self, amount, description=''):
        # check to see if have right amount of funds
        if self.check_funds(amount):
            return False
        else:
            self.balance -= amount
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
    
    def get_balance(self):
        for amount in self.ledger:
            self.balance += amount

# transfer from 1 category to another
    def transfer(self,amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + self.name)
            self.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False
 
    def check_funds(self, amount):
        if self.balance >= amount:
            # print("Save to deposit")
            return False
        else:
            # print("Insufficiant funds")
            return True  


    def __str__(self):
        print('\v')
        print(f"{'*' * 10}{self.name}{'*' * 10}" '\v')
        for item in self.ledger:
            print(f"{item['description']: <15}  $ {item['amount']:8.2f}" '\v')
        return f'TOTAL: {"$" :>11}{self.balance:9.2f}'

# print(f"{x['description']:<22} {x['amount']:>10}")

# CATERGORIES (name)
initial_deposit = Category('BUDGET')
food = Category('food')
clothing = Category('clothing')
entertainment = Category('entertainment')

# deposit

initial_deposit.deposit(1000, 'Deposit')

# withdraw

initial_deposit.withdraw(10.15, 'Food')
initial_deposit.withdraw(50.00, 'Clothing')
initial_deposit.withdraw(15.89, 'Entertainment')
initial_deposit.withdraw(50, 'Food')

# transfer

initial_deposit.transfer(75, clothing)

print(initial_deposit)

