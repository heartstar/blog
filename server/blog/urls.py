#coding:utf8
from django.urls import path
from . import views


urlpatterns = [
    path('', views.Index),
    path('blog/', views.Blog, name='blog'),
    path('detail/<int:id>', views.Detail, name='detail'),
    path('search/', views.Search, name='search'),
    path('tool/', views.Tools, name='tool'),
]
