from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^todo/lists/$', TemplateView.as_view(template_name='todo/todo-list.html'), name='todo-list'),
    url(r'^todo/lists/(?P<pk>\d+)/$', TemplateView.as_view(template_name='todo/todo_detail.html'), name='todo-detail'),
]
