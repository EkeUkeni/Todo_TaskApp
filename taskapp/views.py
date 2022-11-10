from django.shortcuts import render, redirect
from taskapp.models import Task
from taskapp.forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):

    # print(request.GET['search-area'])
    search_query = request.GET.get('search-area')
    print(search_query)
    if search_query is None or search_query == "":
        tasks = Task.objects.filter(user=request.user)
        count = Task.objects.filter(user=request.user, completed=False).count()
    else:
        tasks = Task.objects.filter(user=request.user, title__icontains=search_query)
        count = Task.objects.filter(user=request.user, completed=False, title__icontains=search_query).count()

    context = {
        "tasks":tasks,
        "count":count,
        "search_query":search_query,
    }

    return render(request, "taskapp/index.html", context)


def create_task(request):
    form = TaskForm()
    title = "Create Task"

    if request.method=="POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            
        return redirect("taskapp:home")

    context = {
        "form":form,
        "title":title,
    }

    return render(request, 'taskapp/task_form.html', context)


def update_task(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(instance=task)
    title = "Update Task"

    if request.method=="POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            
        return redirect("taskapp:home")

    context = {
        "form":form,
        "title":title,
    }

    return render(request, 'taskapp/task_form.html', context)

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)

    if request.method=="POST":
        task.delete()

        return redirect("taskapp:home")

    context = {
        "task":task
    }

    return render(request, "taskapp/task_confirm_delete.html", context)