from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Project

# Create your views here.

@login_required
def projects(request):
    projects = Project.objects.filter(created_by=request.user).order_by('-updated_at')

    return render(
        request,
        'projects/projects.html',
        {
            'projects': projects
        }
    )

@login_required
def create_project(request):
    object_created=False

    if request.method == 'POST':
        project_title = request.POST.get('title')
        project_description = request.POST.get('description')
        project_owner = request.user

        if project_title != "" and project_description != "":
            Project.objects.create(name=project_title, description=project_description, created_by=project_owner)
            object_created=True

    return render(
        request,
        'projects/create_project.html',
        {
            'object_created': object_created
        }
    )

@login_required
def project_details(request, project_id):
    selected_project = Project.objects.filter(created_by=request.user).get(id=project_id)
    return render(
        request,
        'projects/project_details.html',
        {
            'selected_project': selected_project
        }
    )

@login_required
def project_delete(request, project_id):
    selected_project = Project.objects.filter(created_by=request.user).get(id=project_id)
    selected_project.delete()
    return redirect('/projects/list/')

@login_required
def project_edit(request, project_id):
    selected_project = Project.objects.get(id=project_id)

    if request.method == 'POST':
        project_title = request.POST.get('title')
        project_description = request.POST.get('description')

        if project_title != "" and project_description != "":
            selected_project.name = project_title
            selected_project.description = project_description
            selected_project.save()
            return redirect('/projects/list/')

    return render(
        request,
        'projects/project_edit.html',
        {
            "selected_project": selected_project
        }
    )