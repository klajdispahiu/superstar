from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('projects/list/', views.projects, name='projects'),
    path('projects/create/', views.create_project, name='create_project'),
    path('projects/details/<str:project_id>/', views.project_details, name='project_details'),
    path('projects/delete/<str:project_id>/', views.project_delete, name='project_delete'),
    path('projects/edit/', views.project_edit, name='project_edit'),
    path('projects/edit/<str:project_id>/', views.project_edit, name='project_edit'),
    path('projects/<str:project_id>/file/upload/', views.upload_file, name='upload_file'),
    path('projects/<str:project_id>/file/delete/<str:file_id>', views.delete_file, name='delete_file'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
