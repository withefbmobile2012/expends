from django.urls import path
from main.views import home as views
from main.views.home import expense_view

urlpatterns = [
    path('', views.home, name='home'),
    path('expense/', expense_view, name='expense')
]

