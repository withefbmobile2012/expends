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
            return redirect('/expense') 
        
        expenses = Expense.objects.all()
        return render(request, 'expense.html', {'form': form, 'expenses': expenses})
    

class ExpenseUpdateView(View):
    def get(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        form = ExpenseForm(instance=expense)
        return render(request, 'expense_update.html', {'form': form, 'expense': expense})
    
    
class ExpenseDeleteView(View):
    def get(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        return render(request, 'expense_delete.html', {'expense': expense})
    
    def post(self, request, pk):
        expense = Expense.objects.get(pk=pk)
        expense.delete()
        return redirect('/expense')