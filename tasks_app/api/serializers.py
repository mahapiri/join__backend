from rest_framework import serializers
from contacts_app.api.serializer import ContactSerializer
from contacts_app.models import Contact
from tasks_app.models import PRIO_CHOICES, STATUS_CHOICES, Category, Subtask, Task


# Serializer for managing task category data, exposing only the name field.
class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ['id', 'name', 'color']


# Serializer for Subtask model, focusing on subtask description and completion status.
class SubtaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Subtask
        fields = ['id', 'task', 'subtask', 'is_completed']


# Serializer used to create new tasks, including optional subtasks and contacts.
class TaskSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    subtasks = SubtaskSerializer(many=True, required=False)
    category = CategorySerializer(many=False, required=True)
    assigned_contacts = ContactSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'prio',
                  'status', 'assigned_contacts', 'category', 'subtasks']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks', [])
        assigned_contacts_data = validated_data.pop('assigned_contacts', [])
        category_data = validated_data.pop('category', None)

        category_id = category_data.get('id') if category_data else None
        validated_data['category_id'] = category_id
        task = Task.objects.create(**validated_data)

        if subtasks_data:
            for subtask_data in subtasks_data:
                subtask_data['task'] = task
                Subtask.objects.create(**subtask_data)

        if assigned_contacts_data:
            contact_ids = [contact.get('id') for contact in assigned_contacts_data if contact.get('id')]
            task.assigned_contacts.set(contact_ids)
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.get('subtasks', [])
        assigned_contacts_data = validated_data.get('assigned_contacts', [])

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.prio = validated_data.get('prio', instance.prio)
        instance.status = validated_data.get('status', instance.status)

        if subtasks_data:
            for subtask_data in subtasks_data:
                subtask_id = subtask_data.get('id')
                if subtask_id:
                    subtask = Subtask.objects.get(id=subtask_id, task=instance)
                    subtask.subtask = subtask_data.get(
                        'subtask', subtask.subtask)
                    subtask.is_completed = subtask_data.get(
                        'is_completed', subtask.is_completed)
                    subtask.save()
                else:
                    Subtask.objects.create(
                        task=instance,
                        subtask=subtask_data.get('subtask', ''),
                        is_completed=subtask_data.get('is_completed', False)
                    )
        if assigned_contacts_data:
            contact_ids = [contact.get('id') for contact in assigned_contacts_data if contact.get('id')]
            instance.assigned_contacts.set(contact_ids)

        instance.save()
        return instance


# Serializer to return task counts by status and upcoming deadline information.
class TaskCountSerializer(serializers.Serializer):
    tasks_count = serializers.IntegerField()
    to_do_count = serializers.IntegerField()
    in_progress_count = serializers.IntegerField()
    await_feedback_count = serializers.IntegerField()
    done_count = serializers.IntegerField()
    urgent_count = serializers.IntegerField()
    upcoming_deadline = serializers.DateField(allow_null=True)
