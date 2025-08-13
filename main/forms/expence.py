from django import forms
from main.models.expense import Expense, UserSalary



salary = forms.ModelChoiceField(
    queryset=UserSalary.objects.all(),
    empty_label="Ish haqini tanlang", 
    widget=forms.Select(attrs={
        'class': 'form-control',
    })
)

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['salary', 'description', 'amount_spent', 'category', 'date']
        widgets = {
            'salary': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you spend on?'}),
            'amount_spent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class UserSalaryForm(forms.ModelForm):
    class Meta:
        model = UserSalary
        fields = ['total_salary']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Salary Name'}),
            'total_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount'}),
        }