from django.views import View
from django.shortcuts import render, redirect
from main.models.expense import UserSalary
from main.forms import UserSalaryForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class UserSalaryView(View):
    def get(self, request):
        salaries = UserSalary.objects.all()
        return render(request, 'expense_salary.html', {
            'salaries': salaries,
            'form': UserSalaryForm()
        })

    def post(self, request):
        form = UserSalaryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_list')
        salaries = UserSalary.objects.all()
        return render(request, 'expense_salary.html', {
            'salaries': salaries,
            'form': form
        })


@method_decorator(login_required, name='dispatch')
class UserSalaryDeleteView(View):
    def post(self, request, pk):
        salary = get_object_or_404(UserSalary, pk=pk)
        salary.delete()
        return redirect('salary_list')


@method_decorator(login_required, name='dispatch')
class UserSalaryEditView(View):
    def get(self, request, pk):
        salary = get_object_or_404(UserSalary, pk=pk)
        form = UserSalaryForm(instance=salary)
        return render(request, 'expense_salary.html', {
            'form': form,
            'salaries': UserSalary.objects.all(),
            'edit_id': pk
        })

    def post(self, request, pk):
        salary = get_object_or_404(UserSalary, pk=pk)
        form = UserSalaryForm(request.POST, instance=salary)
        if form.is_valid():
            form.save()
        return redirect('salary_list')