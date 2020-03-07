#!/opt/python3/bin/python3
# _*_ coding:utf-8 _*_
# Author: Yong
# 这里放到试图函数里，生成任务ID 入库
from celery_task.auto_check import task_celery
import os,json

ip = ['192.168.56.134','192.168.56.133']
port = 22
user = 'root'
pwd = 'ls3du8'
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
script = os.path.join(ROOT_DIR,'shell.sh')
task_id = []
with open('tmp.json','w') as f:
    for i in ip:
        result = task_celery.delay(i,port,user,pwd,script)
        task_id.append(result.id)
    json.dump(task_id,f)

# result = test_celery2.delay('第二个被执行')
# print(result.id)