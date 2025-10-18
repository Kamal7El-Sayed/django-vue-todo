from django.shortcuts import render
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.urls import reverse_lazy


# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    
    
class TaskDetail(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    
    
class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url =reverse_lazy('tasks:task_list')     # بعد الحفظ هيرجع لصفحة المهام

    
    def form_valid(self, form):
        form.instance.user = self.request.user        # بيربط التاسك بالمستخدم الحالي
        return super().form_valid(form)
    
    
class TaskUpdate(UpdateView):
    model = Task
    form_class = TaskForm  
    template_name = 'tasks/task_form.html'
    success_url =reverse_lazy('tasks:task_list')
    
    
class TaskDelete(DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'
    success_url = reverse_lazy('tasks:task_list')