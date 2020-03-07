#!/opt/python3/bin/python3
# _*_ coding:utf-8 _*_
# Author: Yong
# 放到视图函数里，前端通过任务ID 从redis提取结果，然后入库
from celery.result import AsyncResult
from celery_task.celery import cel
import json
with open('tmp.json') as f:
    task_id = json.load(f)
for id in task_id:
    result = AsyncResult(id=id,app=cel)

    if result.successful():
        print(result.get())
        # result.forget() # 将结果删除,执行完成，结果不会自动删除
        # async.revoke(terminate=True)  # 无论现在是什么时候，都要终止
        # async.revoke(terminate=False) # 如果任务还没有开始执行呢，那么就可以终止。
    elif result.failed():
        print('任务执行失败')
    elif result.status == 'PENDING':
        print('任务等待中被执行')
    elif result.status == 'RETRY':
        print('任务异常后正在重试')
    elif result.status == 'STARTED':
        print('任务已经开始被执行')