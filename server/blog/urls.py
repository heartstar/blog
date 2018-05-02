#coding:utf8

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/menu', views.Menu_list),
    url(r'^api/article/add', views.Article_add),
    url(r'^api/article/query', views.Article_query),
    url(r'^api/article/delete', views.Article_delete),
    url(r'^api/image/query', views.Article_delete),
]
