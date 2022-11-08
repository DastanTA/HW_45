from django.contrib import admin
from django.urls import path
from to_do.views import main_page, create_new, view_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('new/', create_new),
    path('task/', view_task)
]
