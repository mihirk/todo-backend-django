from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

from todo_backend_django.models import TodoItem
from todo_backend_django.serializers import TodoItemSerializer


class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        self.__setitem__('Access-Control-Allow-Origin', '*')
        self.__setitem__('Access-Control-Allow-Headers', 'Content-Type')


def todo_list(request):
    if request.method == 'GET':
        todo_items = TodoItem.objects.all()
        serializer = TodoItemSerializer(todo_items, many=True)
        return JSONResponse(serializer.data)