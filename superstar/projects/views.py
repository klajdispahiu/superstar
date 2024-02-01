from django.contrib.auth.decorators import login_required
from django.shortcuts import render

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
        return render(
        request,
        'projects/create_project.html',
    )