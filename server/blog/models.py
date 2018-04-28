from django.db import models

# Create your models here.

class Menu(models.Model):

    name = models.CharField(u"菜单名称", max_length = 30) 
    flag_use = models.BooleanField(u"启用", default=True)
    na_par = models.CharField(u"上级名称", max_length = 30)
    create_date = models.DateTimeField(u"发布日期", auto_now_add = True, editable=True)
    

 