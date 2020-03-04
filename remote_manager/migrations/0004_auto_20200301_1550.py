# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-01 07:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_manager', '0003_auto_20200301_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosttab',
            name='ip_addr',
            field=models.GenericIPAddressField(verbose_name='系统IP'),
        ),
        migrations.AlterField(
            model_name='hosttab',
            name='login_pwd',
            field=models.CharField(max_length=32, verbose_name='密码'),
        ),
        migrations.AlterField(
            model_name='hosttab',
            name='port',
            field=models.PositiveSmallIntegerField(default=22, unique=True),
        ),
        migrations.AlterField(
            model_name='idctab',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projecttab',
            name='name',
            field=models.CharField(max_length=64, verbose_name='项目名'),
        ),
        migrations.AlterField(
            model_name='projecttab',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='systypetab',
            name='name',
            field=models.CharField(help_text='AIX/redhat6/redhat7/...', max_length=16, unique=True, verbose_name='主机系统类型'),
        ),
        migrations.AlterField(
            model_name='systypetab',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasklogdetailtab',
            name='result',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tasktab',
            name='host_tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_manager.HostTab', verbose_name='关联主机'),
        ),
        migrations.AlterField(
            model_name='tasktab',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='关联账号'),
        ),
    ]