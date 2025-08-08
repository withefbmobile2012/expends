from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.db.models import Sum
import main.forms
import main.models as models


def filtering_daily(request):
    daily = models.Expense.objects.filter(user=request.user, date=timezone.now().date())
    context = {
        "daily_filter": daily
    }
    return render(request, "categories.html", context)


def filtering_weekly(request):
    weekly = models.Expense.objects.filter(user=request.user, date=timezone.now().weekday())
    context = {
        "weekly_filter": weekly
    }
    return render(request, "categories.html", context)


def filtering_monthly(request):
    monthly = models.Expense.objects.filter(user=request.user, date=timezone.now().month)
    context = {
        "monthly_filter": monthly
    }
    return render(request, "categories.html", context)


def filtering_by_categories(request):
    category_filter = models.Expense.objects.filter(users=request.user).values('category__name').annote(total=Sum('amount'))
    context = {
        "category_filter": category_filter
    }
    return render(request, "category.html", context)
