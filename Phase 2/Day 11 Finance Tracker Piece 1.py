#doing pieces of the finance tracker rather than building the whole thing at once its too hard
#first piece:

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

expenses = add_expense(expenses, "Coffee", 3)
expenses = add_expense(expenses, "Book", 15)

for expense in expenses:
     print(expense)