from django.shortcuts import render, redirect
from main.models.expense import Expense
from main.views import *
from django.views import View
from main.forms import ExpenseForm



class ExpenseView(View):
    def get(self, request):
        form = ExpenseForm()
        expenses = Expense.objects.all()
        return render(request, 'index.html', {'form': form, 'expenses': expenses})

    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense') 
        
        expenses = Expense.objects.all()
        return render(request, 'expense.html', {'form': form, 'expenses': expenses})