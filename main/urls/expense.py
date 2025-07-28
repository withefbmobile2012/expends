from main.views.expense import Expense
from django.urls import path

path = [
    path('expense/', Expense.as_view(), name='expense'),
    path('expense/<int:id>/', Expense.as_view(), name='expense_detail'),
    path('expense/<int:id>/edit/', Expense.as_view(), name='expense_edit'),
]