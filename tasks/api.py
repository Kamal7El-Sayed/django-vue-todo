from .serilaizers import TaskSeriaizers
from .models import Task
from rest_framework import viewsets
from rest_framework.decorators import api_view


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-id')
    serializer_class = TaskSeriaizers