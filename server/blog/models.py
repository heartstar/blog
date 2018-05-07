from django.db import models

# Create your models here.

class Menu(models.Model):

    caption = models.CharField(u"名称", max_length = 30, default="") 
    flag_use = models.BooleanField(u"启用", default=True)
    code = models.IntegerField(u"编码", default=0)
    na_par = models.CharField(u"上级", max_length = 30)
    create_date = models.DateTimeField(u"发布日期", auto_now_add = True, editable=True)


class Article(models.Model):
   
    title = models.CharField(u'标题', max_length = 100)
    category = models.PositiveIntegerField(u'类型', default=0)
    create_date = models.DateTimeField(u"发布日期", auto_now_add = True, editable=True)
    show = models.BooleanField(u'展示', default=True)     #是否显示
    visits = models.PositiveIntegerField(u'阅读量', default=0)     #访问次数
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)
    keyword = models.CharField(u'关键字', max_length = 100, default='')
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def increase_views(self):
        self.visits += 1
        self.save(update_fields=['visits']) 
        

class Image(models.Model):

    title = models.CharField(u'名称', max_length=100)
    name = models.CharField(u'姓名', max_length=30)
    path = models.CharField(u'路径', max_length=255)
    stem_from = models.CharField(u'来源', max_length=255)

    def __unicode__(self):
        return self.title







# python3 manage.py makemigrations 
# python3 manage.py migrate  
    

 