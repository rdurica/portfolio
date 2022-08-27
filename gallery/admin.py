from django.contrib import admin

from gallery.models import Item


# Register your models here.
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "url",
        "is_enabled",
    ]
