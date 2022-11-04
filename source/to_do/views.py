from django.shortcuts import render
from to_do.models import ToDoList


def main_page(request):
    list_to_do = ToDoList.objects.order_by('created_at')
    context = {
        'list_to_do': list_to_do
    }
    return render(request, 'index.html', context)
