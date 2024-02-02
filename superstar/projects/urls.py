from django.urls import path
from . import views

urlpatterns = [
    path('projects/list/', views.projects, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/details/<str:project_id>/', views.project_details, name='project_details'),
]