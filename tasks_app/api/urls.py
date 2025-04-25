from django.urls import path
from rest_framework.urls import app_name
from tasks_app.api.views import ApiView, TaskCreateView, TaskDeleteView, TaskDetailView, TaskListView, TaskUpdateView

app_name = 'tasks_api'

urlpatterns = [
    path('', ApiView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
    path('all/', TaskListView.as_view(), name='all'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='delete'),
]