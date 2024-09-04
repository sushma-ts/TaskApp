from django.urls import path
from .views import TaskListCreateAPIView, TaskRetrieveUpdateDestroyAPIView, task_list, task_edit, task_delete, TaskFormView,SuccessView

urlpatterns = [
    path('task/', TaskListCreateAPIView.as_view(), name='task-list-create'), #RESTAPI list and Add tasks 
    path('task/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task-retrieve-update-destroy'), #RESTAPI update and delete tasks

     path('add', TaskFormView.as_view(), name='task_add'), #To Display List of tasks
    path('list', task_list, name='task_list'), #To Display List of tasks
    path('tasks/<int:pk>/edit/', task_edit, name='task_edit'), #To edit the tasks
    path('tasks/<int:pk>/delete/', task_delete, name='task_delete'), #To delete the tasks
    path('success', SuccessView.as_view(), name='success'),
]
