from datetime import timedelta
from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum
import main.models as models


def dashboard(request):
    today = timezone.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    daily = models.Expense.objects.filter(user=request.user, date=today)
    weekly = models.Expense.objects.filter(user=request.user, date__gte=end_of_week)
    monthly = models.Expense.objects.filter(user=request.user, date__month=timezone.now().month)
    by_categories = models.Expense.objects.filter(user=request.user).values('category__name').annotate(total=Sum('amount'))
    context = {
        "daily": daily,
        "weekly": weekly,
        "monthly": monthly,
        "by_categories": by_categories,
    }
    return render(request, "charts.html", context)