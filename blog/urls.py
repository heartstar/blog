#coding:utf8

from django.conf.urls import include, url
from . import views

urlpattens = [
    url(r'^index/', include(views.Index))
    url(r'^detail/(?P<id>\d+)/$',views.Detail, name="blog_detail"),
]
