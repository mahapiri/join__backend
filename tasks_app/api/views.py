# from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks_app.api.serializers import CategorySerializer, SubtaskSerializer, TaskCountSerializer, TaskSerializer
from tasks_app.models import Category, Subtask, Task


# View for rendering the API overview page, requiring login.
class ApiView(TemplateView):
    template_name = 'tasks_app/api/api_view.html'
    login_url = '/accounts/login/'


# API view to list all tasks, requiring login.
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# View for retrieving, updating, or deleting a specific task, requiring login.
class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# API view to create a new task, requiring login.
class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskSerializer


# API view to provide a summary of task counts based on different criteria, requiring login.
class TaskSummaryView(APIView):
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

        upcoming_task = Task.objects.filter(prio='urgent').exclude(status='done').order_by('due_date').first()
        urgent_task = Task.objects.filter(prio='urgent').exclude(status='done').count()

        counts['upcoming_deadline'] = upcoming_task.due_date if upcoming_task else None
        counts['urgent_count'] = urgent_task
        return Response(TaskCountSerializer(counts).data)


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class SubtaskDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Subtask.objects.all()
    serializer_class = SubtaskSerializer
