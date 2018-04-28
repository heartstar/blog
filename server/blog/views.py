
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from blog.models import Menu
from .serializers import MenuSerializer



@api_view(['GET', 'POST'])
def Menu_list(request):   

    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        res ={
            'data': serializer.data,
            'code': 200
        }
        return Response(res)
