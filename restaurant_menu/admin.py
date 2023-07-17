from django.contrib import admin
from .models import Item


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("meal", "category", "status")
    list_filter = ("status", "category")
    search_fields = ("meal", "description")
    ordering = ("meal",)


admin.site.register(Item, MenuItemAdmin)