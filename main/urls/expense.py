from django.urls import path
from main.views.expense import ExpenseView, ExpenseEditView, ExpenseDeleteView, UserSalaryView

urlpatterns = [
    path('', ExpenseView.as_view(), name='expense_list'),
    path('<int:id>/', ExpenseView.as_view(), name='expense_detail'),
    path('<int:pk>/edit/', ExpenseEditView.as_view(), name='expense_edit'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('salaries/', UserSalaryView.as_view(), name='salary_list'),
]