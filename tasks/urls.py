from django.urls import path, include
from rest_framework import routers
from .api import TaskViewSet
from .views import TaskList, TaskDetail ,TaskCreate ,TaskDelete ,TaskUpdate ,landing ,logout_view

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

app_name ="tasks"

urlpatterns = [
    
    
    path('myapi/', include(router.urls)),
    
    path('', TaskList.as_view(), name="task_list"),
    path('<int:pk>', TaskDetail.as_view(), name="task_detail"),    
    path ('add/', TaskCreate.as_view(), name="task_create"),


    path('edit/<int:pk>',TaskUpdate.as_view(), name='task_update'),
    path('delete/<int:pk>', TaskDelete.as_view(), name='task_delete'),
    
    
    path('',landing, name='landing'),
    path('logout/',logout_view, name='logout'),
   # path('<int:pk>/toggle/', toggle_task_status, name='task_toggle'),
   
   
]
    








