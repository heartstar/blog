
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from blog.models import Menu, Article
from blog import models
from .serializers import MenuSerializer, ArticleSerializer

from django.core.paginator import Paginator
import json
from django.views.decorators.csrf import csrf_exempt #解决跨域



@api_view(['GET'])
def Menu_list(request):   

    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response({'data':serializer.data, 'code':200})



@csrf_exempt
@api_view(['GET', 'POST'])
def Article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all();
        serializer = ArticleSerializer(articles, many=True)
        return Response({'data':serializer.data, 'code':200})


    if request.method == 'POST':
        req = json.loads(request.body)

        category = req['category']
        title = req['title']
        #show = int(req['show'], 0)
        create_date = req['createDate']
        content = req['content']

        if req:
            models.Article.objects.create(category = category, title = title, create_date = create_date, content = content)

        return Response({'data':'成功', 'code':200})

