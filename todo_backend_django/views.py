from rest_framework import status
from rest_framework.views import APIView

from todo_backend_django.JSONResponse import JSONResponse

from todo_backend_django.models import TodoItem
from todo_backend_django.serializers import TodoItemSerializer


class TodoList(APIView):
    def get(self, request, format=None):
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TodoItemSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        TodoItem.objects.all().delete()
        return JSONResponse(None, status=status.HTTP_204_NO_CONTENT)

class Todo(APIView):
    def get(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
            serializer = TodoItemSerializer(todoItem)
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponse(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
            todoItem.delete()
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        return JSONResponse(None, status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk, format=None):
        try:
            todoItem = TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            return JSONResponse(None, status=status.HTTP_400_BAD_REQUEST)
        serializer = TodoItemSerializer(data=request.DATA, instance=todoItem, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=status.HTTP_200_OK)
        return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
