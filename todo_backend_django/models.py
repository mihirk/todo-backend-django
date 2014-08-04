from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField()