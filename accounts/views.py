from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login               # علشان نعمل تسجيل دخول تلقائي


# Create your views here.

def signup (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)                     # تسجيل دخول تلقائي بعد التسجيل
            return redirect('tasks:task_list')       # يرجع لقائمة المهام
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form' : form})
    
    
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Accounts App 👋")
