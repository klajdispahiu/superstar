from django.urls import path
from . import views

urlpatterns = [
    path('task/list/<str:project_id>/', views.tasks, name='tasks'),
    path('task/create/<str:project_id>/', views.create_task, name='create_task'),
    path('task/single/<str:task_id>/', views.single_task, name='single_task'),
    path('task/delete/<str:task_id>/', views.task_delete, name='task_delete'),
    path('task/edit/<str:task_id>/', views.task_edit, name='task_edit'),
]   
