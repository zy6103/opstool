# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-01 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_manager', '0004_auto_20200301_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecttab',
            name='pro_type',
            field=models.CharField(choices=[('---', '---'), ('app', 'app'), ('db2', 'db2'), ('oracle', 'oracle'), ('mysql', 'mysql')], default='---', max_length=8, verbose_name='项目主机类型'),
        ),
    ]
