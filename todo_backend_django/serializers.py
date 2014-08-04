from rest_framework import serializers
from todo_backend_django.models import TodoItem


class TodoItemSerializer(serializers.ModelSerializer):
    pk = serializers.Field()
    title = serializers.CharField(max_length=256, required=False, blank=True)
    completed = serializers.BooleanField(required=False, default=None)

    def restore_object(self, attrs, instance=None):
        if instance:
            instance.title = attrs.get('title', instance.title)
            instance.completed = attrs.get('completed', instance.completed)
            return instance
        return TodoItem(**attrs)

    class Meta:
        model = TodoItem
        fields = ('title', 'completed')