# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Menu, Article


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('caption', 'code')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('articleId', 'title', 'visits', 'category', 'keyword', 'show', 'content', 'update_time', 'create_date')