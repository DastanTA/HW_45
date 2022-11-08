from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from to_do.models import ToDoList, STATUS_CHOICES


def main_page(request):
    if request.method == "POST":
        task_id = request.GET.get('id')
        task = ToDoList.objects.get(id=task_id)
        task.delete()
    list_to_do = ToDoList.objects.order_by('created_at')
    context = {
        'list_to_do': list_to_do
    }
    return render(request, 'index.html', context)


def create_new(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'create_task.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        name = request.POST.get('name')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        if deadline == "":
            deadline = None
        description = request.POST.get('description')
        new_task = ToDoList.objects.create(name=name, status=status, deadline=deadline, description=description)
        return redirect('view_task', pk=new_task.id)


def view_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    return render(request, 'task.html', {'task': task})
