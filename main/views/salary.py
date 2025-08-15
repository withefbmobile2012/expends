from django.views import View
from django.shortcuts import render, redirect
from main.models.expense import UserSalary
from main.forms import UserSalaryForm
from django.shortcuts import get_object_or_404
from main.models.expense import Expense
from main.forms import ExpenseForm



class UserSalaryView(View):
    def get(self, request):
        salaries = UserSalary.objects.all()
        expenses = Expense.objects.all()  # Add expense history
        form = UserSalaryForm()
        return render(request, 'expense_salary.html', {
            'form': form,
            'salaries': salaries,
            'expenses': expenses  # Send to template
        })

    def post(self, request):
        form = UserSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
        salaries = UserSalary.objects.all()
        expenses = Expense.objects.all()
        return render(request, 'expense_salary.html', {
            'form': form,
            'salaries': salaries,
            'expenses': expenses
        })


class UserSalaryDeleteView(View):
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('/')
        salary = get_object_or_404(UserSalary, pk=pk)
        salary.delete()
        return redirect('salary_list')



class UserSalaryEditView(View):
    def get(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('/')
        salary = get_object_or_404(UserSalary, pk=pk)
        form = UserSalaryForm(instance=salary)
        return render(request, 'expense_salary.html', {
            'form': form,
            'salaries': UserSalary.objects.all(),
            'edit_id': pk
        })


    def post(self, request, pk):
        if not request.user.is_authenticated:
            return redirect('/')
        salary = get_object_or_404(UserSalary, pk=pk)
        form = UserSalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
        return redirect('salary_list')
