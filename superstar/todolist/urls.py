from django.urls import path
from . import views

urlpatterns = [
    path('task/list/<str:project_id>/', views.tasks, name='tasks'),
    path('task/create/<str:project_id>/', views.create_task, name='create_task'),
]