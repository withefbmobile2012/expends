from django.http.response import Http404
from django.shortcuts import  render

import main.models as model


def category_create(request):
    category_c = model.Category.objects.all()

    if request.POST:
        name = request.POST.get("name")
        model.Category.objects.create(
            name=name,
        )

    return render(request, "blank.html", context={"c_create": category_c})



def category_read(request):
    category_r = model.Category.objects.all()

    if request.POST:
        return category_r

    return render(request, "blank.html", context={"c_read": category_r})

def category_update(request, pk):
    try:
        category_u = model.Category.objects.get(pk=pk)
        if request.POST:
            name = request.POST.get("name")
            model.Category.objects.delete(
                name=name,
            )
            model.Category.objects.create(
                name=name,
            )
    except model.Category.objects.DoesNotExists as e:
        return Http404(e)

    return render(request, "blank.html", {"c_update": category_u})


def category_delete(request, pk):
    try:
        category_d = model.Category.objects.get(pk=pk)
    except model.Category.objects.DoesNotExists as d:
        return Http404(d)
    if pk.is_valid():
        category_d.delete()
    return render(request, "blank.html", {"c_delete": category_d})