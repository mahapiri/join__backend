from rest_framework import serializers
from contacts_app.models import Contact
from tasks_app.models import PRIO_CHOICES, STATUS_CHOICES, Category, Subtask, Task

# Task Retrieve

class TaskSubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        # fields = ['pk', 'subtask', 'is_completed']
        fields = '__all__'


class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class TaskContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        # fields = ['pk', 'name']
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    subtasks = TaskSubtasksSerializer(many=True, read_only=True)
    category = TaskCategorySerializer(many=False, read_only=True)
    assigned_contacts = TaskContactSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['pk' ,'title', 'description', 'due_date', 'prio', 'status', 'assigned_contacts', 'category', 'subtasks']


# TASK CREATE 

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['subtask', 'is_completed']


class TaskCreateSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'prio', 'status', 'assigned_contacts', 'category', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks')
        assigned_contacts_data = validated_data.pop('assigned_contacts', [])

        task = Task.objects.create(**validated_data)

        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        
        task.assigned_contacts.set(assigned_contacts_data)
        return task


class TaskCountSerializer(serializers.Serializer):
    tasks_count = serializers.IntegerField()
    to_do_count = serializers.IntegerField()
    in_progress_count = serializers.IntegerField()
    await_feedback_count = serializers.IntegerField()
    done_count = serializers.IntegerField()
    urgent_count = serializers.IntegerField()
    upcoming_deadline = serializers.DateField(allow_null=True)