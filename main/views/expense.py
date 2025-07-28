from django.shortcuts import render
from main.models.expense import Expense
from main.views import *
from django.views import View
from main.models import base



class ExpenseView(base.BaseModel, View):
    def get(self, request):
        expenses = Expense.objects.all()
        return render(request, 'index.html', {'expenses': expenses})