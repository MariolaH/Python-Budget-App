## BUDGET APP

```
OBJECTIVE:

    Input amount of money in bank
    Display inital amount
    Display categories, groceries, entertainment, clothes
    deduct categories from intial deposit 
    Total after deductions are made

```

```
USER INPUT / DISPLAY:

    Input field for intial amount
    List of all the categories
    Input field with name of category and how much spent
    Display total after deductions

```

```
CLASS

    1. Class Catergory
            - instance variable ledger
            -budget categories
                -food
                -clothing
                -entertainment
```

```
    METHODS:

        1. DEPOSIT
            - amount
            - description
                -none give: default to '' (empty string)
                    -(self, amount, description='')
            - append an object to the ledger list in form:
                - {"amount": amount, "description": description}
                    ledger.append({"amount": amount, "description": description})
                        list_name.append(element)
    

        2. WITHDRAW
            -amount
                - store in ledger as a negative number
                - not enough funds, nothing added to ledger
            -RETURN
                - true: if withdrawl took place
                - false if no withdrawl took place
            
        3. GET_BALANCE
            - returns the current balance of budget category
                - based on DEPOSIT
                - based on WITHDRAWLS

        4. TRANSFER
            - accepts an amount and another budget category as arguments
            - add a withdrawl with the amount
                - and description "Transfer to [Destination Budget Category]"
            - add a deposit to the other budget category with the amount
                -and description "Transfer from [Source Budget Category]"
            - If not enough funds:
                - nothing should be added either ledger
            - RETURN:
                - True: if the transfer took place
                - False: otherwise

        5. CHECK_FUNDS
            - accepts an amount as an argument
                - RETURNS
                    - False: if the amount is less than the balance of the budget category
                    - True: otherwise
            - used both by withdraw and transfer method
    
```