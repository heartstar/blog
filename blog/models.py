#coding:utf8

from __future__ import unicode_literals
from django.db import models


#文章
class Article(models.Model):
    
    title = models.CharField('标题', max_length=32)
    category = models.CharField('标签', max_length=50, blank=True)
    pub_date = models.DateTimeField('发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

class Meta:
    ordering = ['-pub_date']
    verbose_name = '文章'
    verbose_name_plural = '文章'


#评论
class Comment(models.Model):

    title = models.CharField('标题', max_length=32)
    category = models.CharField('标签', max_length=50, blank=True)
    pub_date = models.DateTimeField('评论时间', auto_now_add=True, editable=True)
    content = models.TextField(blank=True, null=True)





# 123
# qwe123456