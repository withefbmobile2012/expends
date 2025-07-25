from django.shortcuts import render

import users.forms as forms


def register_user(request):
    form = forms.RegisterUserForm()
    return render(request, "form.html", {"form": form})
