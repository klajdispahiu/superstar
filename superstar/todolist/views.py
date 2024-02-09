from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from projects.models import Project
from todolist.models import Todolist

# Create your views here.

@login_required
def tasks(request, project_id):
    selected_project = Project.objects.filter(created_by=request.user).get(id=project_id)
    
    task_list = Todolist.objects.filter(project=selected_project)

    return render(
        request,
        'todolist/todolist.html',
        {
            'selected_project': selected_project,
            'task_list': task_list
        }
    )

@login_required
def create_task(request, project_id):  
    selected_project = Project.objects.filter(created_by=request.user).get(id=project_id)

    if request.method == 'POST':
        task_name = request.POST.get('name')
        task_description = request.POST.get('description')

        if task_name != '' and task_description != '':
            Todolist.objects.create(
                name=task_name,
                description=task_description,
                created_by=request.user,
                project=selected_project
            )

            task_list = Todolist.objects.filter(project=project_id)
            return render(
                request,
                'todolist/todolist.html',
                {
                    'selected_project': selected_project,
                    'task_list': task_list
                }
            ) 


    return render(
        request,
        'todolist/create_todolist.html',
        {
            'selected_project': selected_project
        }
    )

@login_required
def single_task(request, task_id):

    selected_task = Todolist.objects.get(id=task_id)

    return render (
        request,
        'todolist/single_task.html',
{
    'selected_task' : selected_task
}
    )
    
@login_required
def task_delete(request, task_id):
    selected_task = Todolist.objects.get(id=task_id)
    selected_task.delete()

    selected_project=Project.objects.filter(created_by=request.user).get(id=selected_task.project.id)

    task_list = Todolist.objects.filter(project=selected_task.project.id)
    return render(
        request,
        'todolist/todolist.html',
        {
            'selected_project': selected_project,
            'task_list': task_list
        }
    ) 
    
@login_required
def task_edit(request, task_id):
    selected_task = Todolist.objects.get(id=task_id)

    if request.method == 'POST':
        task_name = request.POST.get('name')
        task_description = request.POST.get('description')

        if task_name != "" and task_description != "":
            selected_task.name = task_name
            selected_task.description = task_description
            selected_task.save()
            
            return render(
                request, 
                'todolist/single_task.html',
                {
                    'selected_task' : selected_task

                }
            )

    return render(
        request, 
        'todolist/edit_todolist.html',
        {
            'selected_task' : selected_task

        }
    )