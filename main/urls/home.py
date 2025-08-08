from django.urls import path
import main.views.home as views

urlpatterns = [
    path('', views.home, name='home'),
    path('expense/', views.expense_view, name='expense')
]

