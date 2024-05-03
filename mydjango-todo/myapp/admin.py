from django.contrib import admin
from .models import Todo

# Register your models here.Item,
# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin) :
#     list_display = [
#         "name",
#         "note"
#     ]

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin) :
    list_display = [
        "name", "description", "updated", "completed"
    ]