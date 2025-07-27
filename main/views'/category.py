from decorator import decorator
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404

import main.models as models

def category_list(request):
    categories = models.Category.objects.all()
    return render(request, "categories.html")

