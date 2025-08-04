from django.shortcuts import render, get_object_or_404, redirect

import main.forms
import main.models as model


def category_create(request):
    category_c = model.Category.objects.all()

    if request.POST:
        name = request.POST.get("name")
        model.Category.objects.create(
            name=name,
        )

    return render(request, "categories.html", context={"c_create": category_c})


def categories_detail(request, pk):
    category_detail = get_object_or_404(model.Category, pk=pk)
    context = {
        "c_detail": category_detail
    }
    return render(request, "categories.html", context)

def categories_list(request):
    category_list = model.Category.objects.all()
    context = {
        "c_list": category_list
    }
    return render(request, "categories.html", context)

def categories_update(request, pk):
    category_update = get_object_or_404(model.Category, pk=pk)
    if request.POST:
        form = main.forms.CategoryForm
        if form.is_valid():
            form.save()
            return redirect("/category/list")
        form = main.forms.CategoryForm(instance=category_update)
        context = {
            "form": form,
            "title": "Category Update"
        }
        return render(request, "crud_form.html", context)
    else:
        return redirect("/")

def categories_delete(pk):
    category_delete = get_object_or_404(model.Category, pk=pk)
    category_delete.delete()
    return redirect("/")