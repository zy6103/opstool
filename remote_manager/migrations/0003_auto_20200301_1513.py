# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-03-01 07:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_manager', '0002_auto_20200301_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='project_tab',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_manager.ProjectTab'),
        ),
    ]
