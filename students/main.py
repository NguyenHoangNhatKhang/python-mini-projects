class Expense():
    def __init__(self,amount,description,date,category):
        self.amount = amount
        self.description = description 
        self.date = date 
        self.category = category 
    def __str__(self): 
        return f"{self.date} / {self.amount}円 / {self.category} / {self.description}"
    
class ExpenseManager():
    def __init__(self,expenses):
        self.expenses = expenses    

    def add_expenses(self):
        self.expenses = []
        return self.expenses().append()