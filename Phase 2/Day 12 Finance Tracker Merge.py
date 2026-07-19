#merging the pieces from day 11 to soon have the full project completed

class Expense:
    def __init__ (self, item, amount):
        self.item = item
        self.amount = amount
    
    def __str__(self):
        return f"{self.item}: {self.amount}$"
    
expenses = []

def add_expense(expenses, item, amount):
        new_expense = Expense(item, amount)
        expenses.append(new_expense)
        return expenses

Interactions = {1:"add expense",
                2:"exit"}

print(Interactions)


while True:

    interaction = int(input("which action do you want to do?: "))

    if interaction in Interactions:
        if interaction == 1:
            item = input("enter the item you want to add: ")
            amount = int(input("how much will this item cost?: "))
            expenses = add_expense(expenses, item, amount)

            for x in expenses:
                print(x)
            print(f"you just added {item} and it will cost {amount}$")

    
        elif interaction == 2:
            break

    else:
        print("error, invalid iption.")


