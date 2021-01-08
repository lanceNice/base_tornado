#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @File : push_task.py
# @Desc : 推送大屏数据

import requests
import json
from tasks.celery import app


# 使用队列 进行数据推送
# push_task.project_update_task.delay(city_code, project_id)

@app.task
def project_update_task(city_code, project_id):
    # url = "http://192.168.1.134:8090/project_update_task"
    url = "https://api.yooticloud.cn/middle/project_update_task"
    # url = "http://hzbj.test.yt/middle/project_update_task"
    data = {
        "city_code": city_code,
        "project_id": project_id
    }
    try:
        requests.put(url, data=json.dumps(data), timeout=5)
    except:
        pass
