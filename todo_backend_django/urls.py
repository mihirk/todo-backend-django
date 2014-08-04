from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from todo_backend_django import views

urlpatterns = patterns('',
                       url(r'^$', RedirectView.as_view(url='/todos')),
                       url(r'^todos$', views.TodoList.as_view()),
                       url(r'^todo/(?P<pk>[0-9]+)$', views.Todo.as_view()),
    # Examples:
    # url(r'^$', 'todo_backend_django.views.home', name='home'),
    # url(r'^todo_backend_django/', include('todo_backend_django.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
