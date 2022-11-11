from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from to_do.models import ToDoList, STATUS_CHOICES
from to_do.forms import TaskForm


def main_page(request):
    list_to_do = ToDoList.objects.order_by('created_at')
    context = {
        'list_to_do': list_to_do
    }
    return render(request, 'index.html', context)


def create_new(request, *args, **kwargs):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'create_task.html', {'form': form})
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


def update_view(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'name': task.name,
            'description': task.description,
            'status': task.status,
            'deadline': task.deadline
        })
        context = {"task": task, 'form': form}
        return render(request, "update.html", context)
    elif request.method == "POST":
        task.name = request.POST.get("name")
        task.description = request.POST.get("description")
        task.status = request.POST.get("status")
        task.deadline = request.POST.get("deadline")
        task.save()
        return redirect("view_task", pk=task.pk)


def delete_task(request, pk):
    task = get_object_or_404(ToDoList, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('main')
