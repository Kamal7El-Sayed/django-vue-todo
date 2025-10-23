from django.shortcuts import render,redirect
from .models import Task
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TaskForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout



# Create your views here.

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'user_name': request.user.username})



class TaskList(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    login_url = 'login'  # لو مش عامل login يتحول لصفحة login

    def get_queryset(self):
            # عرض المهام الخاصة بالمستخدم فقط
        return Task.objects.filter(user=self.request.user)

    
class TaskDetail(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'
    
    
class TaskCreate(LoginRequiredMixin,CreateView):
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
    
    
def landing(request):
    # لو المستخدم عامل تسجيل دخول، يروح على صفحة المهام
    if request.user.is_authenticated:
        print("⚠️ [INFO] Authenticated user tried to access the landing page:", request.user.username)
        return redirect('tasks:task_list')
    print("✅ [INFO] Anonymous visitor accessed the landing page.")
    # لو مش عامل تسجيل دخول، يشوف صفحة البداية
    return render(request, 'landing.html')



def logout_view(request):
    logout(request)
    return redirect('login')  # أو 'landing' لو عايز يرجع للصفحة الرئيسية
