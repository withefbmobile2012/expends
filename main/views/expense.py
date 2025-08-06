from django.shortcuts import render, redirect
from main.models.expense import Expense
from main.views import *
from django.views import View
from main.forms import ExpenseForm
from django.shortcuts import get_object_or_404




class ExpenseView(View):
    def get(self, request):
        expenses = Expense.objects.all()
        return render(request, 'index.html', {
            'form': ExpenseForm(),
            'expenses': expenses
        })

    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('expense_list')


class ExpenseEditView(View):
    def get(self, request, pk):
        expenses = Expense.objects.all()
        expense = get_object_or_404(Expense, pk=pk)
        return render(request, 'index.html', {
            'form': ExpenseForm() if pk is None else None,  # no add form while editing
            'expenses': expenses,
            'edit_form': ExpenseForm(instance=expense),
            'edit_id': pk
        })

    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/expense')


class ExpenseDeleteView(View):
    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        expense.delete()
        return redirect('/expense')