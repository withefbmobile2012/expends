from django.views import View
from django.shortcuts import render, redirect
from main.models.expense import UserSalary
from main.forms import UserSalaryForm

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