#coding:utf8

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from blog.models import Article
from django.http import Http404

# Create your views here.

def Index(request):
    
    post_list = Article.objects.all()
    return render(request, 'index.html',{'posts':post_list})


def Detail(request, id):
    
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request,'detail.html',{'post':post})

    