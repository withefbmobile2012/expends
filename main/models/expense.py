from django.db import models
from django.utils import timezone


class UserSalary(models.Model):
    total_salary = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    remaining_salary = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        # When creating, initialize remaining_salary = total_salary
        if self.pk is None and self.remaining_salary is None:
            self.remaining_salary = self.total_salary
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Total Salary: {self.total_salary or 'Not set'}"
    


class Expense(models.Model):
    salary = models.ForeignKey(
        UserSalary, on_delete=models.CASCADE, related_name='expenses'
    )
    amount_spent = models.DecimalField(
        max_digits=15, decimal_places=2, null=True, blank=True
    )
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True, related_name='expenses', blank=True
    )
    date = models.DateField(default=timezone.now)
    cashback_percent = models.DecimalField(
        max_digits=5, decimal_places=2, default=0, help_text="Cashback percent (0-100)"
    )

    def __str__(self):
        return f"{self.description} - {self.amount_spent} on {self.date}"

    def cashback_amount(self):
        return (self.amount_spent or 0) * (self.cashback_percent or 0) / 100

    def save(self, *args, **kwargs):
        if self.pk:
            old_expense = Expense.objects.get(pk=self.pk)
            self.salary.remaining_salary += old_expense.amount_spent or 0

        cashback_amount = (self.amount_spent or 0) * (self.cashback_percent or 0) / 100
        self.salary.remaining_salary -= self.amount_spent or 0
        self.salary.remaining_salary += cashback_amount

        if self.salary.remaining_salary < 0:
            self.salary.remaining_salary = 0

        self.salary.save()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.salary.remaining_salary += self.amount_spent or 0
        self.salary.save()
        super().delete(*args, **kwargs)