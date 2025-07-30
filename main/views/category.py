from django.shortcuts import render, get_object_or_404
from django.http import Http404
from main import models
from main.models import Category
from rest_framework.exceptions import NotFound as NotFoundErr

categories = []

def category_list(request):
    return render(request, 'index.html')



def category_c(request):
    category_cr = models.Category.objects.all()

    if request.POST:
        name = request.POST.get("name")
        models.User.objects.create(
            name=name,
        )
        categories.append(category_cr)

    return render(request, "categories.html", context={"created": category_cr})

def category_r(request):
    category_read = categories

    if request.POST:
        return category_read

    return render(request, "categories.html", context={"c_list": category_read})

def category_up(request, pk):
    try:
        category = models.Category.objects.get(pk=pk)
    except models.Category.DoesNotExists:
        return render (status=get_object_or_404(NotFoundErr))
    if category.is_valid():
        name = Category.name()
        name = models.models.CharField(max_length=100)
        category.save()
        return render(request, "categories.html", {"c_up": category})
    else:
        ...