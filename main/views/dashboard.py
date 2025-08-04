from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

import main.forms
import main.models as model


def filtering_daily(request):
    daily = main.models.Expense.objects.filter(user=request.user, date=timezone.now().date())
    context = {
        "daily_filter": daily
    }
    return render(request, "categories.html", context)


def filtering_weekly(request):
    weekly = main.models.Expense.objects.filter(user=request.user, date=timezone.now().weekday())
    context = {
        "weekly_filter": weekly
    }
    return render(request, "categories.html", context)


def filtering_monthly(request):
    monthly = main.models.Expense.objects.filter(user=request.user, date=timezone.now().month)
    context = {
        "monthly_filter": monthly
    }
    return render(request, "categories.html", context)


def filtering_by_categories(request, pk):
    category = model.Category.objects.get(pk=pk)
    filtering = main.models.Expense.objects.filter(user=request.user).values('category__name').annotate(total=Sum('amount'))
