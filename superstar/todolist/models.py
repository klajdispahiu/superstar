from django.db import models

from projects.models import Project
from account.models import User

# Create your models here.

class Todolist(models.Model):    
    id = models.AutoField(primary_key=True, auto_created=True, editable=False)
    project = models.ForeignKey(Project, related_name='todolists', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='todolists', on_delete=models.CASCADE)

    def __str__(self):
      	return self.name
