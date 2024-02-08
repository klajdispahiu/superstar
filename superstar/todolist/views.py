from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from projects.models import Project

# Create your views here.

@login_required
def tasks(request, project_id):
    selected_project = Project.objects.filter(created_by=request.user).get(id=project_id)
    
    task_list = []

    
    return render(
        request,
        'todolist/todolist.html',
        {
            'selected_project': selected_project,
            'task_list': task_list
        }
    )