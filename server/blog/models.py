from django.db import models

# Create your models here.

class Menu(models.Model):

    name = models.CharField(u"菜单名称", max_length = 30) 
    flag_use = models.BooleanField(u"启用", default=True)
    na_par = models.CharField(u"上级", max_length = 30)
    create_date = models.DateTimeField(u"发布日期", auto_now_add = True, editable=True)


class Article(models.Model):
   
    title = models.CharField(u'标题', max_length = 100)
    category = models.PositiveIntegerField(u'类型', max_length = 10)
    create_date = models.DateTimeField(u"发布日期", auto_now_add = True, editable=True)
    show = models.BooleanField(u'展示', default=True)     #是否显示
    visits = models.PositiveIntegerField(u'阅读量', default=0)     #访问次数
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    content = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def increase_views(self):
        self.visits += 1
        self.save(update_fields=['visits']) 







# python3 manage.py makemigrations 
# python3 manage.py migrate  
    

 