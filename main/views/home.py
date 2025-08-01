from django.shortcuts import render



def home(request):
    return render(request, 'index.html')


def expense_view(request):
    return render(request, 'expense.html')