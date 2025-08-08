from django import forms
from main.models import Expense



class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['salary']  
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }