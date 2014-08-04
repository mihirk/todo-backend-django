from rest_framework import serializers
from todo_backend_django.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    pk = serializers.Field()
    title = serializers.CharField(max_length=256)
    completed = serializers.BooleanField()

    class Meta:
        model = TodoItem
        fields = ('title', 'completed')