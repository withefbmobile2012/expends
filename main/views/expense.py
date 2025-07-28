from django.views import View
from django.shortcuts import render
from main.views import *
from main.models.expense import Expense

class Expense(View):
    def get(self, request):
        expenses = Expense.objects.all()
        return render(request, 'expense_list.html', {'expenses': expenses})