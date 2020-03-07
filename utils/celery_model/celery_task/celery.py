#!/opt/python3/bin/python3
# _*_ coding:utf-8 _*_
# Author: Yong

from celery import Celery

cel = Celery('celery_demo',
             broker='redis://127.0.0.1/0',
             backend='redis://127.0.0.1/1',
            # 包含以下两个任务文件，去相应的py文件中找任务，对多个任务做分类
             include=['celery_task.auto_check'])
cel.conf.timezone = 'Asia/Shanghai'
cel.conf.enable_utc = False