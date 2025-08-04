from django.urls import path
from main.views.expense import ExpenseView, ExpenseUpdateView, ExpenseDeleteView

urlpatterns = [
    path('expense/', ExpenseView.as_view(), name='expense'),
    path('expense/<int:id>/', ExpenseView.as_view(), name='expense_detail'),
    path('expense/<int:id>/edit/', ExpenseView.as_view(), name='expense_edit'),
    path('expense/update/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('expense/delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),
]