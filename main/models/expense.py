from django.db import models
from django.utils import timezone



class UserSalary(models.Model):
    total_salary = models.DecimalField(
        max_digits=1000000000,
        decimal_places=2,
        null=True,
        blank=True
    )

    def remaining_salary(self):
        spent = sum(exp.amount_spent or 0 for exp in self.expenses.all())
        return (self.total_salary or 0) - spent

    def __str__(self):
        return f"Total Salary: {self.total_salary or 'Not set'}"
    


class Expense(models.Model):
    salary = models.ForeignKey(UserSalary, on_delete=models.CASCADE, related_name='expenses')
    amount_spent = models.DecimalField(max_digits=10000000, decimal_places=2, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='expenses', blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description} - {self.amount_spent} on {self.date}"

    @property
    def remaining_salary_after_this(self):
        return self.salary.total_salary - self.amount_spent


class Salary(models.Model):
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    remaining_salary = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.remaining_salary <= 0:
            self.delete()
            return
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Salary: {self.amount} (Remaining: {self.remaining_salary})"