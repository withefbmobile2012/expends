from django.shortcuts import render, redirect
from django.contrib import messages
from main import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_user(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username, password)

            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                messages.success(request, 'Logged in successfully')
                return redirect('/home')
            else:
                messages.error(request, 'Invalid credentials')
        messages.error(request, f'{form.errors}')
        print(form.error_messages)
    form = AuthenticationForm()
    return render(request, "auth/register.html", {"form": form})


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