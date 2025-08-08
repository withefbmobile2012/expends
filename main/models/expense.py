from django.db import models
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

    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    amount_spent = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    description = models.CharField(max_length=200, default="No description")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='OTHER')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.amount_spent} on {self.date}"

    @property
    def remaining_salary_after_this(self):
        return self.salary - self.amount_spent


class UserSalary(models.Model):
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Total Salary: {self.total_salary}"
    

class UserSalary(models.Model):
    total_salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Total Salary: {self.total_salary}"