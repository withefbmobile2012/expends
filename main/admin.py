from django.contrib import admin

import main.models as models


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    search_fields = ("name", "username", "description", "filter_name")
    list_filter = ("added_at",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "added_at")
    list_display_links = ("id", "name")


class ExpenseAdmin(models.Expense):
    list_display = ('description', 'amount_spent', 'salary', 'remaining', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('description', 'tags')


