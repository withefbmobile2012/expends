from main.models import *
from main.urls.expense import path as expense_urls
from main.views import *
from main.views.expense import Expense
from django.urls import path, include
from main.views.home import home
from main.views.users import register_user, login_user, logout_user, profile

__all__ = [
    'ExpenseView',
    'expense_urls',
    'Expense',
]


urlpatterns = [
    path('expense/', include(expense_urls)),
    path('', home, name='home'),
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/', profile, name='profile'),

    path('category/', include('main.urls.category')),
]