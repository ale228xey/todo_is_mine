from django.urls import path

from todo.views import TaskView, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', TaskView.as_view(), name='main'),

    path('create_task', CreateTask.as_view(), name='create_task'),
    path('update_task/<int:pk>', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>', DeleteTask.as_view(), name='delete_task'),
]
