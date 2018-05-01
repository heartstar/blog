#coding:utf8

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/menu', views.Menu_list),
    url(r'^api/article', views.Article_list),
]
