# Generated by Django 2.0 on 2018-04-30 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_menu_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='na_par',
            field=models.CharField(max_length=30, verbose_name='上级'),
        ),
    ]