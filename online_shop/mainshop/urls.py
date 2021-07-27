from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mainshop.models import Posts


urlpatterns = [
    url(r'^$', ListView.as_view(queryset = Posts.objects.all().order_by('-date'),
    template_name = 'mainshop/index.html'))
]