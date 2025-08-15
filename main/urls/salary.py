from django.urls import path
from main.views.salary import UserSalaryView, UserSalaryDeleteView, UserSalaryEditView

urlpatterns = [
    path('', UserSalaryView.as_view(), name='salary_list'),
    path('salaries/<int:pk>/edit/', UserSalaryEditView.as_view(), name='salary_edit'),
    path('salaries/<int:pk>/delete/', UserSalaryDeleteView.as_view(), name='salary_delete'),
]