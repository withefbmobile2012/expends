from django.shortcuts import render, redirect
from django.contrib import messages
from main import forms

def login_user(request):
    if request.POST:
        form = forms.LoginUserForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                messages.success(request, 'Logged in successfully')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
    form = forms.LoginUserForm()
    return render(request, "auth/login.html", {"form": form})


def logout_user(request):
    if request.user.is_authenticated:
        messages.success(request, 'Logged out successfully')
    else:
        messages.error(request, 'You are not logged in')
    return redirect('/')



def register_user(request):
    if request.POST:
        form = forms.RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('/')
    form = forms.RegisterUserForm()
    return render(request, "auth/register.html", {"form": form})


def profile(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You need to be logged in to view your profile')
        return redirect('/login/')
    user = request.user
    expenses = user.expense_set.all()
    categories = user.category_set.all()
    return render(request, "auth/profile.html", {
        "user": user,
        "expenses": expenses,
        "categories": categories
    })