from django.shortcuts import redirect, render, get_object_or_404

import main.models as models

categories = [

]


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

    return render(request, "categories.html", context={"created": category_cr})
