# -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'name', 'flag_use', 'na_par', 'create_date')
