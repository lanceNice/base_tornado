# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 16:42
# @Author  : lance
# @File    : app_utils.py
# @Software: PyChar
# app相关工具类
import hashlib
import time


# 得到app相关的信息
def get_app_info():
    app_id = str(time.time()).replace('.', '')
    if len(app_id) > 16:
        app_id = app_id[:16]
    else:
        add = 16 - len(app_id) % 16 if len(app_id) % 16 else 0
        app_id += 'x' * add
    app_key = hashlib.md5(app_id.encode('utf-8')).hexdigest().upper()
    return app_id, app_key
