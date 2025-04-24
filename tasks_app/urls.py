from django.urls import path, re_path, reverse_lazy
from django.views.generic import RedirectView

from tasks_app.views import TaskListView

app_name = 'tasks'

urlpatterns = [
    path('all/', TaskListView.as_view(), name='all'),
    re_path(r'^all/.+', RedirectView.as_view(url=reverse_lazy('tasks:all'))),
]
