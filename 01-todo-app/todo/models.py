from django.db import models

class TodoItem(models.Model):
    title = models.CharField(max_length=200, help_text="Short description of the task")
    description = models.TextField(blank=True, null=True, help_text="Optional details")
    due_date = models.DateTimeField(help_text="When the task should be completed")
    is_resolved = models.BooleanField(default=False, help_text="Whether the task is done")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
