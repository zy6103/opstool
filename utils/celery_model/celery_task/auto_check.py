#!/opt/python3/bin/python3
# _*_ coding:utf-8 _*_
# Author: Yong

from celery_task.celery import cel
import os,sys

# ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(ROOT_DIR)
from utils.celery_model.remote_running import RemoteHost

@cel.task
def task_celery(ip,port,user,pwd,script):
    ser = RemoteHost(ip,port,user,pwd,script)
    ser.check()
    ser.close()

    return "%s 执行完成" % ip