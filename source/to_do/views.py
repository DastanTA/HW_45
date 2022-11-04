from django.shortcuts import render
from to_do.models import ToDoList


def main_page(request):
    list_to_do = ToDoList.objects.order_by('created_at')
    context = {
        'list_to_do': list_to_do
    }
    return render(request, 'index.html', context)

def create_new(request):
    if request.method == "GET":
        return render(request, 'new_task.html')
    elif request.method == "POST":
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        new_task = ToDoList.objects.create(description=description, status=status, deadline=deadline)
        context = {'new_task': new_task}
        return render(request, 'info.html', context)