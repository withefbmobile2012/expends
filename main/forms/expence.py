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
    class Meta:
        model = Expense
        fields = ['salary', 'description', 'amount_spent', 'category', 'date']
        widgets = {
            'salary': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'What did you spend on?'}),
            'amount_spent': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Amount Spent'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }



class UserSalaryForm(forms.ModelForm):
    class Meta:
        model = UserSalary
        fields = ['total_salary']
        widgets = {
            'total_salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary',
                'min': '0.01',  # HTML5 client-side
                'step': '0.01'
            }),
        }

    def clean_total_salary(self):
        total_salary = self.cleaned_data.get('total_salary')
        if total_salary is None or total_salary < Decimal('0.01'):
            raise forms.ValidationError("Salary must be at least $0.01")
        return total_salary

        