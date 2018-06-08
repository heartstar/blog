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
#爬取
import requests
from bs4 import BeautifulSoup
import re



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


@csrf_exempt
@api_view(['GET'])
def Tools_query(request):
    
    if request.method == 'GET':
        tools = []
        url = 'http://tool.oschina.net'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
        html = requests.get(url, headers = header)
        soup = BeautifulSoup(html.text,'html.parser')
        all_nav = soup.find('div', class_='tool_index').find_all('ul', 'nav-list')

        for ul in all_nav:
            all_nav_li = ul.find_all('li')
            for li in all_nav_li:
                href = li.find('a')['href'] if li.find('a')['href'].find('http') >-1 else url+li.find('a')['href']
                title = li.find('a').text
                tools.append({'href':href, 'title':title})
            
        return Response({'data':tools, 'code':200}) 



@csrf_exempt
@api_view(['GET'])
def Movie_query(request):
    
    if request.method == 'GET':
        movies = []
        url = 'https://www.diediaow.com/frim/index1.html'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36'}
        html = requests.get(url, headers = header)
        soup = BeautifulSoup(html.text,'html.parser')
        all_li = soup.find('ul', class_='ul').find_all('li')

        for li in all_li:
            href_ = li.find('a', class_='jqr')['href']     
            href = 'https://www.diediaow.com/play/'+ re.sub("\D", "", href_) +'-0-0.html'
            title = li.find('a', class_='jqr')['title']
            img = li.find('img', alt=title)['src']
            movies.append({'href':href, 'title':title, 'img':img})
            
        return Response({'data':movies, 'code':200})
