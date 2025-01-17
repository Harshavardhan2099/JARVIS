from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Title: {self.title} Completed: {self.completed}"