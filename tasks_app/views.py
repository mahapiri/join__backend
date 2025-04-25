from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from tasks_app.models import Category, Subtask, Task


# View to list all tasks with login required
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks_app/task_list.html'
    login_url = '/accounts/login/'


# View to display details of a specific task with login required
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'tasks_app/task_detail_list.html'
    login_url = '/accounts/login/'


# View to create a new task with login required
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks_app/task_create.html'
    login_url = '/accounts/login/'
    fields = ['title', 'description', 'due_date', 'prio',
              'status', 'assigned_contacts', 'category']
    success_url = 'tasks_app/subtask_create.html'

    # Redirect to subtask creation page after task creation

    def get_success_url(self):
        return reverse('tasks:subtask_create', kwargs={'pk': self.object.pk})


# View to update an existing task with login required
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks_app/task_update.html'
    fields = ['title', 'description', 'due_date', 'prio',
              'status', 'assigned_contacts', 'category']

    # Redirect to task detail page after updating the task

    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.object.pk})


# View to delete a task with login required
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:all')
    template_name = 'tasks_app/task_delete.html'


# View to create a new subtask for a task with login required
class SubtaskCreateView(LoginRequiredMixin, CreateView):
    model = Subtask
    template_name = 'tasks_app/subtask_create.html'
    login_url = '/accounts/login/'
    fields = ['subtask', 'is_completed']

    # Add task ID to context data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    # Assign the correct task to the subtask before saving

    def form_valid(self, form):
        task_id = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        form.instance.task = task
        return super().form_valid(form)

    # Redirect to task detail page after subtask creation

    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.kwargs.get('pk')})


# View to update an existing subtask with login required
class SubtaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Subtask
    template_name = 'tasks_app/subtask_update.html'
    fields = ['subtask', 'is_completed']
    pk_url_kwarg = 'subtask_id'

    # Add subtask ID to context data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtask_id'] = self.kwargs.get('subtask_id')
        return context

    # Redirect to task detail page after updating the subtask

    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.kwargs.get('pk')})


# View to create a new category for tasks with login required
class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'tasks_app/category_create.html'
    login_url = '/accounts/login/'
    fields = ['name', 'color']

    # Redirect to task creation page after category creation

    def get_success_url(self):
        return reverse('tasks:create')
