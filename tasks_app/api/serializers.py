from rest_framework import serializers
from contacts_app.models import Contact
from tasks_app.models import PRIO_CHOICES, STATUS_CHOICES, Category, Subtask, Task


# Serializer for creating and managing task-related data, including subtasks, categories, and assigned contacts.
class TaskSubtasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


# Serializer for managing task category data, exposing only the name field.
class TaskCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Serializer for managing contact data associated with tasks.
class TaskContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# Main serializer for Task model, including related subtasks, categories, and assigned contacts.
class TaskSerializer(serializers.ModelSerializer):
    subtasks = TaskSubtasksSerializer(many=True, read_only=True)
    category = TaskCategorySerializer(many=False, read_only=True)
    assigned_contacts = TaskContactSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


# Serializer for Subtask model, focusing on subtask description and completion status.
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = '__all__'


# Serializer used to create new tasks, including optional subtasks and contacts.
class TaskCreateSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, required=False)
    assigned_contacts = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all(), many=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_contacts_data = validated_data.pop('assigned_contacts', [])

        task = Task.objects.create(**validated_data)

        if subtasks_data:
            for subtask_data in subtasks_data:
                subtask_data['task'] = task
                Subtask.objects.create(**subtask_data)

        task.assigned_contacts.set(assigned_contacts_data)
        return task


# Serializer to return task counts by status and upcoming deadline information.
class TaskCountSerializer(serializers.Serializer):
    tasks_count = serializers.IntegerField()
    to_do_count = serializers.IntegerField()
    in_progress_count = serializers.IntegerField()
    await_feedback_count = serializers.IntegerField()
    done_count = serializers.IntegerField()
    urgent_count = serializers.IntegerField()
    upcoming_deadline = serializers.DateField(allow_null=True)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
