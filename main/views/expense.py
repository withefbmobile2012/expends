from django.shortcuts import render, redirect
from main.models.expense import Expense
from main.views import *
from django.views import View
from main.forms import ExpenseForm
from django.shortcuts import get_object_or_404
from main.models.expense import UserSalary
from main.views.category import categories_detail
from main.forms.expence import ExpenseForm, UserSalaryForm



class ExpenseView(View):
    def get(self, request):
        expenses = Expense.objects.all()
        salaries = UserSalary.objects.all()

        return render(request, 'index.html', {
            'form': ExpenseForm(),
            'expenses': expenses,
            'salaries': salaries,  
            'salary_set': salaries.exists(),
            'categories': categories_detail(request, Expense, 'expense_list'),
        })

    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            selected_salary = expense.salary  
            selected_salary.total_salary -= expense.amount_spent
            selected_salary.save()
            expense.save()
            return redirect('expense_list')

        return render(request, 'index.html', {
            'form': form,
            'expenses': Expense.objects.all(),
            'salaries': UserSalary.objects.all(),
            'form_errors': form.errors
        })
    
    

class ExpenseEditView(View):
    def get(self, request, pk):
        expenses = Expense.objects.all()
        expense = get_object_or_404(Expense, pk=pk)
        return render(request, 'index.html', {
            'form': ExpenseForm() if pk is None else None,
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
    

def get(self, request):
    expenses = Expense.objects.all()
    salaries = UserSalary.objects.all()

    selected_salary = salaries.first() 

    return render(request, 'index.html', {
        'form': ExpenseForm(),
        'expenses': expenses,
        'salaries': salaries,
        'salary_set': salaries.exists(),
        'selected_salary': selected_salary,
        'categories': categories_detail(request, Expense, 'expense_list'),
    })


class UserSalaryView(View):
    def get(self, request):
        salaries = UserSalary.objects.all()
        form = UserSalaryForm()
        return render(request, 'expense_salary.html', {'form': form, 'salaries': salaries})

    def post(self, request):
        form = UserSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salaries')
        salaries = UserSalary.objects.all()
        return render(request, 'expense_salary.html', {'form': form, 'salaries': salaries})