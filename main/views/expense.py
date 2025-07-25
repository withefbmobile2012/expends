from django.shortcuts import render, get_object_or_404
from django.views import View
from main.models.expense import ExpenseView
from django.urls import path
from main.views import *

expense_urls = [
    path('expense/', ExpenseView.as_view(), name='expense'),
    path('expense/<int:id>/', ExpenseView.as_view(), name='expense_detail'),
    path('expense/<int:id>/edit/', ExpenseView.as_view(), name='expense_edit'),
]