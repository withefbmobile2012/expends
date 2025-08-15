from django.shortcuts import render, redirect
from main.models import Expense
from main.forms import ExpenseForm 
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'index.html')


@login_required
def expense_view(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/expense')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all()
    return render(request, 'expense.html', {'form': form, 'expense': expenses})


