from django.urls import path
from main.views import home as views

urlpatterns = [
    path('', views.home, name='home'),
    path('expense/', views.expense_view, name='expense_view'),
]

