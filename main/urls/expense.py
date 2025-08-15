from django.urls import path
from main.views.expense import ExpenseView, ExpenseEditView, ExpenseDeleteView
from main.views.salary import UserSalaryView, UserSalaryDeleteView, UserSalaryEditView


urlpatterns = [
    path('', ExpenseView.as_view(), name='expense_list'),
    path('<int:pk>/edit/', ExpenseEditView.as_view(), name='expense_edit'),
    path('<int:pk>/delete/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('salary', UserSalaryView.as_view(), name='salary_list'),
    path('salary/<int:pk>/edit/', UserSalaryEditView.as_view(), name='salary_edit'),
    path('salary/<int:pk>/delete/', UserSalaryDeleteView.as_view(), name='salary_delete'),
]