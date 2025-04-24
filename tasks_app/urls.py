from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView

from tasks_app.views import CategoryCreateView, SubtaskCreateView, SubtaskUpdateView, TaskCreateView, TaskDeleteView, TaskListView, TaskDetailView, TaskUpdateView

app_name = 'tasks'

urlpatterns = [
    path('all/', TaskListView.as_view(), name='all'),
    re_path(r'^all/.+', RedirectView.as_view(url=reverse_lazy('tasks:all'))),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('category/create', CategoryCreateView.as_view(), name='category_create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('<int:pk>/subtask/create/', SubtaskCreateView.as_view(), name='subtask_create'),
    path('<int:pk>/subtask/update/<int:subtask_id>/', SubtaskUpdateView.as_view(), name='subtask_update'),
]
