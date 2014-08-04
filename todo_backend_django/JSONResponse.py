from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer


class JSONResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
        self.__setitem__('Access-Control-Allow-Origin', '*')
        self.__setitem__('Access-Control-Allow-Headers', 'Content-Type')
        self.__setitem__('Access-Control-Allow-Methods', 'GET,HEAD,POST,DELETE,OPTIONS,PUT')
