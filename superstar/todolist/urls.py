from django.urls import path
from . import views

urlpatterns = [
    path('task/list/<str:project_id>/', views.tasks, name='tasks'),
]