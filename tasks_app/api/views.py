from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import generics

from tasks_app.api.serializers import TaskCreateSerializer, TaskSerializer
from tasks_app.models import Task


class ApiView(TemplateView):
    template_name = 'tasks_app/api/api_view.html'
    login_url = '/accounts/login/'


class TaskDetailView(LoginRequiredMixin, generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskListView(LoginRequiredMixin, generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateView(LoginRequiredMixin, generics.CreateAPIView):
    serializer_class = TaskCreateSerializer


class TaskUpdateView(LoginRequiredMixin, generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class TaskDeleteView(LoginRequiredMixin, generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer