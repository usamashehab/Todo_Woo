from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Todo(models.Model):
    name = models.CharField(max_length=100)
    dateCreated = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    dateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
