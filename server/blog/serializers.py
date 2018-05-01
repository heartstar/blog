# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Menu, Article


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'flag_use', 'na_par', 'create_date')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'visits', 'category', 'content', 'update_time', 'create_date')