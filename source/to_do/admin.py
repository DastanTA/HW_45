from django.contrib import admin
from to_do.models import ToDoList


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['name']
    fields = ['id', 'name', 'description', 'status', 'deadline', 'created_at']
    

admin.site.register(ToDoList, ToDoAdmin)
