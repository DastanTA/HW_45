from django.contrib import admin
from django.urls import path
from to_do.views import main_page, create_new, view_task, update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name="main"),
    path('new/', create_new, name="add_task"),
    path('task/<int:pk>', view_task, name="view_task"),
    path('task/<int:pk>/update', update_view, name='update_task'),
]
