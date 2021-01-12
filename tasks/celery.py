#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @File : celery.py
# @Desc :


from celery import Celery
from celery.schedules import crontab
from conf import profile


# MINUTES = 6
# redis_url = "redis://{host}:{port}/{db}".format(**settings['redis'])
# rabbit_url = "amqp://{user}:{password}@{host}:{port}/{vhost}".format(**settings['rabbitmq'])
#
# tasks = ['tasks.push_task', "tasks.clear_img_task"]
# app = Celery('tasks', backend=redis_url, broker=rabbit_url, include=tasks)
#
# beat_schedule = {
#     "celery_clear_img": {
#         "task": "tasks.clear_img_task.clear_file",  # 执行的函数
#         "schedule": crontab(minute="*/{}".format(MINUTES)),  # every minute 每分钟执行
#         "args": ()  # # 任务函数参数
#     }
# }
#
# app.conf.update(
#     result_expires=3600 if profile != 'prod' else 86400,
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Asia/Shanghai',
#     enable_utc=True,
#     beat_schedule=beat_schedule
# )
