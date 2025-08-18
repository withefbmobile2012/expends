from django import forms
from main.models.expense import Expense, UserSalary
from decimal import Decimal



salary = forms.ModelChoiceField(
    queryset=UserSalary.objects.all(),
    empty_label="Ish haqini tanlang", 
    widget=forms.Select(attrs={
        'class': 'form-control',
    })
)

class ExpenseForm(forms.ModelForm):
    cashback_percent = forms.DecimalField(
        label="Cashback (%)",
        min_value=0,
        max_value=100,
        decimal_places=2,
        required=False,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cashback % (optional)'})
    )

    class Meta:
        model = Expense
        fields = ['salary', 'description', 'amount_spent', 'category', 'date', 'cashback_percent']
        widgets = {
            'salary': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you spend on?'}),
            'amount_spent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount Spent'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cashback_percent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cashback % (optional)'}),
        }

    def clean_cashback_percent(self):
        val = self.cleaned_data.get('cashback_percent')
        return val if val is not None else Decimal('How much cashback do you get?')


class UserSalaryForm(forms.ModelForm):
    class Meta:
        model = UserSalary
        fields = ['total_salary']
        widgets = {
            'total_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary',
                'min': '0.01', 
                'step': '0.01'
            }),
        }

    def clean_total_salary(self):
        total_salary = self.cleaned_data.get('total_salary')
        if total_salary is None or total_salary < Decimal('0.01'):
            raise forms.ValidationError("Salary must be at least $0.01")
        return total_salary

