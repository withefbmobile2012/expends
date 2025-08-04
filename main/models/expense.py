from django.db import models
from main.models import base
from django.utils import timezone


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('BILLS', 'Bills'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('TRAVEL', 'Travel'),
        ('HEALTH', 'Health'),
        ('OTHER', 'Other'),
    ]

    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Total monthly income")
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, help_text="Amount spent")
    description = models.CharField(max_length=200, default="No decription!", help_text="Description of the expense")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    tags = models.CharField(max_length=100, blank=True, help_text="Optional tags (comma-separated)")
    date = models.DateField(default=timezone.now)

    @property
    def remaining(self):
        return self.salary - self.amount_spent

    def __str__(self):
        return f"{self.description} - {self.amount_spent} on {self.date}|"