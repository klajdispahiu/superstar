from django.urls import path
from . import views

urlpatterns = [
    path('projects/list/', views.projects, name='projects'),
]