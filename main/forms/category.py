from django import forms

import main.models as model

class CategoryForm(forms.ModelForm):
    class Meta:
        model = model.Category
        fields = "__all__"
