from django.shortcuts import render, get_object_or_404, redirect

import main.forms as forms
import main.models as model


def categories_detail(request, pk):
    if request.user.is_authenticated:
        category_detail = get_object_or_404(model.Category, pk=pk)
        context = {
            "category_detail": category_detail
        }
    else:
        return redirect("/")
    return render(request, "categories.html", context)


def categories_list(request):
    if request.user.is_authenticated:
        category_list = model.Category.objects.all()
        context = {
            "category_list": category_list
        }
    else:
        return redirect("/")
    return render(request, "categories.html", context)


def category_create(request):
    if request.user.is_authenticated:
        if request.POST:
            form = forms.CategoryForm
            if form.is_valid():
                form.save()
                return redirect("/category/list")
        form = forms.CategoryForm()
        context = {
            "form": form
        }
    else:
        return redirect("/")
    return render(request, "category_create.html", context)


def category_update(request, pk):
    if request.user.is_authenticated:
        obj = get_object_or_404(model.Category, pk=pk)
        if request.POST:
            form = forms.CategoryForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect("/category/list")
        form = forms.CategoryForm(instance=obj)
        context = {
            "form": form
        }
        return render(request, "category_update.html", context)
    else:
        return redirect("/")


def category_delete(request, pk):
    if request.user.is_authenticated:
        obj = get_object_or_404(model.Category, pk=pk)
        obj.delete()
        return redirect("/category/list")
    else:
        return redirect("/")
