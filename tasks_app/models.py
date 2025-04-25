from random import randrange
from django.db import models
from contacts_app.models import Contact


# Priority choices for tasks
PRIO_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("urgent", "Urgent")
]


# Status choices for tasks
STATUS_CHOICES = [
    ("to_do", "To do"),
    ("in_progress", "In progress"),
    ("await_feedback", "Await feedback"),
    ("done", "Done"),
]


# Category model to define different categories for tasks with a random color assigned
class Category(models.Model):
    name = models.CharField(max_length=256)
    color = models.CharField(max_length=256, editable=False)

    def __str__(self):
        return self.name

    # Override the save method to assign a random color when a category is created

    def save(self, *args, **kwargs):
        self.color = self.get_random_color()
        return super().save(*args, **kwargs)

    # Generate a random hex color for the category

    def get_random_color(self):
        num = randrange(100000, 1000000)
        self.color = '#' + str(num)
        return self.color


# Task model representing tasks with title, description, priority, status, and category
class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=1024, blank=True)
    due_date = models.DateField()
    prio = models.CharField(choices=PRIO_CHOICES, blank=True, null=True)
    status = models.CharField(choices=STATUS_CHOICES, default="to_do")
    assigned_contacts = models.ManyToManyField(
        Contact, blank=True, related_name='tasks')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        ordering = ["due_date"]

    def __str__(self):
        return self.title

    # Override the save method to ensure priority is null if empty
    def save(self, *args, **kwargs):
        if self.prio == "":
            self.prio = None
        return super().save(*args, **kwargs)


# Subtask model representing subtasks associated with a specific task
class Subtask(models.Model):
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name="subtasks")
    subtask = models.CharField(max_length=1024)
    is_completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Subtask"
        verbose_name_plural = "Subtasks"
        ordering = ["task"]

    def __str__(self):
        return self.subtask
