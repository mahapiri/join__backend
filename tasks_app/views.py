from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from contacts_app.models import Contact
from tasks_app.models import Subtask, Task

# Create your views here.
class TaskListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        tasks = Task.objects.all()
        subtasks = Subtask.objects.all()
        ctx = {'tasks': tasks, 'subtasks': subtasks}
        return render(request, 'tasks_app/task_list.html', ctx)
