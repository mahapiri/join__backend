from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView
from tasks_app.models import Category, Subtask, Task

# Create your views here.
class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks_app/task_list.html'
    login_url = '/accounts/login/'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['subtasks'] = Subtask.objects.all()
    #     return context
    

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name ='tasks_app/task_detail_list.html'
    login_url = '/accounts/login/'
    # queryset = Task.objects.prefetch_related('subtasks')


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks_app/task_create.html'
    login_url = '/accounts/login/'
    fields = ['title', 'description', 'due_date', 'prio', 'status', 'assigned_contacts', 'category']
    success_url = 'tasks_app/subtask_create.html'

    def get_success_url(self):
        return reverse('tasks:subtask_create', kwargs={'pk': self.object.pk})
       

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'tasks_app/task_update.html'
    fields = ['title', 'description', 'due_date', 'prio', 'status', 'assigned_contacts', 'category']

    # def form_valid(self, form):
    #      task_id = self.kwargs.get('pk')
    #      task = get_object_or_404(Task, pk=task_id)
    #      form.instance.task = task
    #      return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.object.pk })
    

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:all')
    template_name = 'tasks_app/task_delete.html'


class SubtaskCreateView(LoginRequiredMixin, CreateView):
    model = Subtask
    template_name = 'tasks_app/subtask_create.html'
    login_url = '/accounts/login/'
    fields = ['subtask', 'is_completed']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pk'] = self.kwargs.get('pk')
        return context

    def form_valid(self, form):
        task_id = self.kwargs.get('pk')
        task = get_object_or_404(Task, pk=task_id)
        form.instance.task = task
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.kwargs.get('pk')})


class SubtaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Subtask
    template_name = 'tasks_app/subtask_update.html'
    fields = ['subtask', 'is_completed']
    pk_url_kwarg = 'subtask_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subtask_id'] = self.kwargs.get('subtask_id')
        return context
    
    # def form_valid(self, form):
    #     subtask_id = self.kwargs.get('subtask_id')
    #     subtask = get_object_or_404(Subtask, subtask_id=subtask_id)
    #     form.instance.subtask = subtask
    #     return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('tasks:detail', kwargs={'pk': self.kwargs.get('pk')})

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'tasks_app/category_create.html'
    login_url = '/accounts/login/'
    fields = ['name', 'color']

    def get_success_url(self):
        return reverse('tasks:create')