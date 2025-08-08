from django.urls import path
from main.views.expense import ExpenseView, ExpenseEditView, ExpenseDeleteView

urlpatterns = [
    path('expense/', ExpenseView.as_view(), name='expense_list'),
    path('expense/<int:id>/', ExpenseView.as_view(), name='expense_detail'),
    path('expense/<int:pk>/edit/', ExpenseEditView.as_view(), name='expense_edit'),
    path('expense/<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
]