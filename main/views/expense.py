from django.shortcuts import render, redirect
from main.models.expense import Expense
from main.views import *
from django.views import View
from main.forms import ExpenseForm
from django.shortcuts import get_object_or_404
from main.models.expense import UserSalary




class ExpenseView(View):
    def get(self, request):
        expenses = Expense.objects.all()
        salary_obj = UserSalary.objects.first()

        return render(request, 'index.html', {
            'form': ExpenseForm(),
            'expenses': expenses,
            'salary_set': bool(salary_obj),
            'total_salary': salary_obj.total_salary if salary_obj else 0,
        })

    def post(self, request):
        form = ExpenseForm(request.POST)
        salary_obj = UserSalary.objects.first()

        if not salary_obj:
            salary_input = request.POST.get('salary')
            if not salary_input:
                return render(request, 'index.html', {
                    'form': form,
                    'expenses': Expense.objects.all(),
                    'salary_error': 'Please enter your salary.'
                })
            salary_obj = UserSalary.objects.create(total_salary=salary_input)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.salary = salary_obj.total_salary
            salary_obj.total_salary -= expense.amount_spent
            salary_obj.save()
            expense.save()
            return redirect('expense_list')

        return render(request, 'index.html', {
            'form': form,
            'expenses': Expense.objects.all(),
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