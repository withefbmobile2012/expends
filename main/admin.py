from django.contrib import admin

import main.models as models


# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    search_fields = ("name", "username", "description")
    list_filter = ("added_at",)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "added_at")
    list_display_links = ("id", "name")


@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("id", "amount", "added_at", "description", "date")
    list_display_links = ("id", "description")


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    ...