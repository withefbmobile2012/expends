from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from main.models.expense import Expense, UserSalary
from main.forms.expence import ExpenseForm, UserSalaryForm
from main.views.category import categories_detail


class ExpenseView(View):
    def get(self, request):
        print("User authenticated:", request.user.is_authenticated)  # Debugging line
        if not request.user.is_authenticated:
            return redirect('/')
        expenses = Expense.objects.all()
        # Add cashback_amount for each expense
        expenses_with_cashback = []
        for e in expenses:
            e.cashback_amount = e.cashback_amount()
            expenses_with_cashback.append(e)
        salaries = UserSalary.objects.all()
        return render(request, 'expense.html', {
            'form': ExpenseForm(),
            'expenses': expenses_with_cashback,
            'salaries': salaries,
            'salary_set': salaries.exists(),
            # 'categories': categories_detail(request, Expense, 'expense_list'),
        })

    def post(self, request):
        print("User authenticated:", request.user.is_authenticated)  
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            selected_salary = expense.salary
            # Only update remaining_salary, not total_salary
            # selected_salary.total_salary -= expense.amount_spent  # REMOVE THIS LINE
            # Expense model's save() will handle remaining_salary update
            expense.save()
            return redirect('expense_list')

        return render(request, 'index.html', {
            'form': form,
            'expenses': Expense.objects.all(),
            'salaries': UserSalary.objects.all(),
            'form_errors': form.errors
        })


@method_decorator(login_required, name='dispatch')
class ExpenseEditView(View):
    def get(self, request, pk):
        expenses = Expense.objects.all()
        expense = get_object_or_404(Expense, pk=pk)
        return render(request, 'index.html', {
            'form': ExpenseForm(),
            'expenses': expenses,
            'edit_form': ExpenseForm(instance=expense),
            'edit_id': pk
        })

    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect('expense_list')


@method_decorator(login_required, name='dispatch')
class ExpenseDeleteView(View):
    def post(self, request, pk):
        expense = get_object_or_404(Expense, pk=pk)
        expense.delete()
        return redirect('expense_list')


@method_decorator(login_required, name='dispatch')
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