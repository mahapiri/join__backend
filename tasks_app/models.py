from tabnanny import verbose
from django.db import models

from contacts_app.models import Contact

PRIO_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("urgent", "Urgent")
]

STAUS_CHOICES = [
    ("to_do", "To do"),
    ("in_progress", "In progress"),
    ("await_feedback", "Await feedback")
]


class Category(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, blank=True)
    due_date = models.DateField()
    prio = models.CharField(choices=PRIO_CHOICES, blank=True)
    status = models.CharField(choices=STAUS_CHOICES, default="to_do")
    assigned_contacts = models.ManyToManyField(Contact, blank=True, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["due_date"]
    
    def __str__(self):
        return self.title


class Subtask(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    subtask = models.CharField(max_length=1024)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Subtask"
        verbose_name_plural = "Subtasks"
        ordering = ["task"]

    def __str__(self):
        return self.subtask


