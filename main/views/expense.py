from django.shortcuts import render
from main.views import *
from main.models.expense import Expense
from main.models import base


class Expense(base.BaseModel):
    def get(self, request):
        expenses = Expense.objects.all()
        return render(request, 'expense_list.html', {'expenses': expenses})