from django.contrib import admin
from to_do.models import ToDoList


class ToDoAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'deadline']
    list_filter = ['status']
    search_fields = ['name']
    exclude = []
    

admin.site.register(ToDoList, ToDoAdmin)
