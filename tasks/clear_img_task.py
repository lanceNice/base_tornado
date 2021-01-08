#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File : middle_celery.py
# @Desc : 定时清除图片


from tasks.celery import app

@app.task
def clear_file():
    pass
