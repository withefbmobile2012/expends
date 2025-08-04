from django import forms
from .models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['salary', 'amount_spent', 'description', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


