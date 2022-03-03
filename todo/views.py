from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from todo.models import Task


class TaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class CreateTask(CreateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'create_task.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UpdateTask(UpdateView):
    model = Task
    fields = ['title', 'description']
    template_name = 'update_task.html'
    success_url = '/'


class DeleteTask(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = '/'
