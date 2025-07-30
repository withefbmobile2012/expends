from django.db import models
from main.models import base
from django.utils import timezone



class Expense(base.BaseModel):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description or 'Expense'} - {self.amount} on {self.date}"