from django.urls import path
from rest_framework.urls import app_name
from tasks_app.api.views import ApiView, CategoryCreateView, CategoryListView, SubtaskDestroyView, TaskCreateView, TaskDetailView, TaskListView, TaskSummaryView

app_name = 'tasks_api'

urlpatterns = [
    path('view/', ApiView.as_view()),
    path('', TaskListView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view()),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('summary/', TaskSummaryView.as_view(), name='summary'),
    path('category/', CategoryListView.as_view(), name='category'),
    path('category/create/', CategoryCreateView.as_view(), name='category-create'),
    path('subtask/delete/<int:pk>/', SubtaskDestroyView.as_view(), name='subtask-delete'),
]