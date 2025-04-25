from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks_app.api.serializers import TaskCountSerializer, TaskCreateSerializer, TaskSerializer
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


class TaskSummaryView(LoginRequiredMixin, APIView):
    def get(self, request):
        counts = {
            'tasks_count': Task.objects.count(),
            'to_do_count': Task.objects.filter(status='to_do').count(),
            'in_progress_count': Task.objects.filter(status='in_progress').count(),
            'await_feedback_count': Task.objects.filter(status='await_feedback').count(),
            'done_count': Task.objects.filter(status='done').count(),
            'urgent_count': Task.objects.filter(prio='urgent').count(),
            'upcoming_deadline': Task.objects.filter(prio='urgent').order_by('due_date').first()
        }
        counts['upcoming_deadline'] = counts['upcoming_deadline'].due_date if counts['upcoming_deadline'] else None
        return Response(TaskCountSerializer(counts).data)
