#coding:utf8

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from blog.models import Menu, Article, Image
from blog import models
from .serializers import MenuSerializer, ArticleSerializer

from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage  #分页
import json
from django.views.decorators.csrf import csrf_exempt #解决跨域
from django.db.models import F, Q
import requests



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
        keyword = req['keyword']
        art_id = req.get('id') 

        if art_id:
            models.Article.objects.filter(articleId=art_id).update(category = category, keyword = keyword, title = title, show = show, content = content)
        else:
            models.Article.objects.create(category = category, title = title, keyword = keyword, show = show, content = content)

        return Response({'data':'成功', 'code':200})


@csrf_exempt
@api_view(['GET', 'POST'])
def Article_query(request):

    if request.method == 'GET':

        category_id = request.GET.get('paramsId')

        if (category_id != 'undefined'):
            articles = Article.objects.filter(category=int(category_id)).order_by('-update_time')
        else:
            articles = Article.objects.all().order_by('-update_time')

        articlesTotal = articles.count() 
        paginator = Paginator(articles, int(request.GET.get('pageSize')))
        

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
def Article_search(request):
    print(request.GET.get('str'))
    search_str = request.GET.get('str')
    strs = Article.objects.filter(Q(keyword__icontains=search_str) | Q(title__icontains=search_str) | Q(content__icontains=search_str))
    articlesTotal = strs.count() 
    serializer = ArticleSerializer(strs, many=True)
    return Response({'data':serializer.data, 'total':articlesTotal, 'code':200})


@csrf_exempt
@api_view(['GET'])
def Article_detail(request):

    if request.method == 'GET':
        art_id = str(request.GET.get('id'))
        detail = models.Article.objects.filter(articleId=art_id)
        models.Article.objects.filter(articleId=art_id).update(visits = F('visits') + 1)
        serializer = ArticleSerializer(detail, many=True)
        return Response({'data':serializer.data, 'code':200})


@csrf_exempt
@api_view(['GET'])
def Article_delete(request):

    if request.method == 'GET':
        if request.GET.get('id'):
            models.Article.objects.filter(articleId=request.GET.get('id')).delete()

        return Response({'data':'成功', 'code':200})


@csrf_exempt
@api_view(['GET'])
def Msg_send(request):

    if request.method == 'GET':
        url = 'http://drea.cc/api/chat.php?msg='+ request.GET.get('msg') +'&uid=drea_bbs_chat'
        ori = requests.get(url).json()
        return Response({'data':ori, 'code':200})


