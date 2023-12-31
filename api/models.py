from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    completed   = models.BooleanField(default=False, blank=True, null=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tasks')
    

    def __str__(self):
        return f'{self.id} - {self.title}'