from django.db import models
from django.utils.timezone import now

from account.models import User

# Create your models here.

class Project(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=now, editable=False)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class ProjectFile(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    project = models.ForeignKey(Project, related_name='files', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    attachment = models.FileField(upload_to='projectfiles')

    def __str__(self):
        return self.name

class ProjectNote(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    project = models.ForeignKey(Project, related_name='notes', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
