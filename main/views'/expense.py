from models.expense import Expense


class ExpenseView:
    def __init__(self, expense: Expense):
        self.expense = expense

    def display(self):
        return f"Expense: {self.expense.description or 'No description'} | Amount: {self.expense.amount} | Date: {self.expense.date}"
    
    def update_amount(self, new_amount):
        self.expense.amount = new_amount
        return f"Updated amount to {self.expense.amount}"
    
    def delete_expense(self):
        return "Expense deleted"