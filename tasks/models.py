from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='task_user' )
    title = models.CharField(max_length=225)
    completed = models.BooleanField(default=False)
    
def __str__(self):
    return self.title



