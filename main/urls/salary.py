from django.urls import path
from main.views.salary import UserSalaryView

urlpatterns = [
    path('', UserSalaryView.as_view(), name='salary_list'),
]