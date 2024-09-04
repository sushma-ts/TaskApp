from rest_framework import generics
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer
from django.views import generic
from django.urls import reverse_lazy
#login required mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save()

class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

#Using form displaying lists, editing and deleting the tasks in frontend

class TaskFormView(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = 'tasks/form.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        # Assign the logged-in user to the Task's user field
        form.instance.user = self.request.user
        return super().form_valid(form)

class SuccessView(generic.TemplateView):
    template_name = 'tasks/success.html'

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/lists.html', {'tasks': tasks})

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/update.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/delete.html', {'task': task})


   