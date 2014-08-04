import json
from django.db import models


class TodoItem(models.Model):
    title = models.CharField(max_length=256)
    completed = models.BooleanField()

class TodoList:
    def __init__(self):
        pass

    @staticmethod
    def json():
        return map(lambda todo_item: todo_item.json(), TodoItem.objects.all())