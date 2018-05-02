
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from blog.models import Menu, Article, Image
from blog import models
from .serializers import MenuSerializer, ArticleSerializer

from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage  #分页
import json
from django.views.decorators.csrf import csrf_exempt #解决跨域



@api_view(['GET'])
def Menu_list(request):   

    if request.method == 'GET':
        menus = Menu.objects.filter(flag_use=1)
        serializer = MenuSerializer(menus, many=True)
        return Response({'data':serializer.data, 'code':200})


@csrf_exempt
@api_view(['POST'])
def Article_add(request):
    if request.method == 'POST':
        req = json.loads(request.body)

        category = req['category']
        title = req['title']
        show = int(req['show'])
        content = req['content']

        if Article.objects.filter(id=req['id']):
            models.Article.objects.filter(id=req['id']).update(category = category, title = title, show = show, content = content)
        else:
            models.Article.objects.create(category = category, title = title, show = show, content = content)

        return Response({'data':'成功', 'code':200})


@csrf_exempt
@api_view(['GET', 'POST'])
def Article_query(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        articlesTotal = Article.objects.count() 
        paginator = Paginator(articles, request.GET.get('pageSize'))
        

        try:
            articless = paginator.page(int(request.GET.get('pageNum')))
        except PageNotAnInteger:
            articless = paginator.page(1)
        except EmptyPage:
            articless = paginator.page(paginator.num_pages)

        serializer = ArticleSerializer(articless, many=True)
        return Response({'data':serializer.data, 'total':articlesTotal, 'code':200})


@csrf_exempt
@api_view(['GET'])
def Article_delete(request):

    if request.method == 'GET':
        if request.GET.get('id'):
            models.Article.objects.filter(id=request.GET.get('id')).delete()

        return Response({'data':'成功', 'code':200})


@csrf_exempt
@api_view(['GET'])
def Image_delete(request):

    if request.method == 'GET':
        if request.GET.get('id'):
            models.Article.objects.filter(id=request.GET.get('id')).delete()

        return Response({'data':'成功', 'code':200})


