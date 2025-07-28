from django.shortcuts import render
from django.contrib import messages

import users.forms as forms


def register_user(request):
    if request.POST:
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
    form = forms.RegisterUserForm()
    return render(request, "auth/register.html", {"form": form})
