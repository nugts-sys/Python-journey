#This is the start of my first bigger project, which is gonna be a finance tracker
#ill add stuff here over the next days of my journey
#pretty excited to see how ill do and if all i precticed before is enough to complete it

class Expense:
    def __init__ (self, item, amount):
        self.item = item
        self.amount = amount
    
    def __str__ (self):

        return f"{self.item}: {self.amount}$"
expenses = []

interactions = {1: "add expense",
             2: "show total spent",
             3: "show all expenses",
             4: "exit"}

def add_expense(expenses):
    item = input("first, enter an item: ")
    try:
        amount = int(input("now enter the amount of that item: "))
    except ValueError:
        amount = -1

    while amount <= 0:
        try:
            amount = int(input("now enter the amount of that item: "))
        except ValueError:
            amount = -1

    new_expense = Expense(item, amount)
    expenses.append(new_expense)
    return expenses
             

print(interactions)

while True:
    interaction_input = int(input("enter the option you want to commit: "))
    if interaction_input == 1:
        expenses = add_expense(expenses)
        for expense in expenses:
            print(expense)

    elif interaction_input == 4:
        break
        

    
