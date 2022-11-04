from django.contrib import admin
from django.urls import path
from to_do.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
]
