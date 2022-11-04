from django.contrib import admin
from to_do.models import ToDoList


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['description', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['description']
    fields = ['id', 'description', 'status', 'deadline', 'created_at']
    

admin.site.register(ToDoList, ToDoAdmin)
