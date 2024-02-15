from django.urls import path
from . import views

urlpatterns = [
    path('projects/list/', views.projects, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/details/<str:project_id>/', views.project_details, name='project_details'),
    path('projects/delete/<str:project_id>/', views.project_delete, name='project_delete'),
    path('projects/edit/', views.project_edit, name='project_edit'),
    path('projects/edit/<str:project_id>/', views.project_edit, name='project_edit'),
    path('projects/<str:project_id>/file/upload/', views.upload_file, name='upload_file')
]