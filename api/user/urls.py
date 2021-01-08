#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tornado.web import url

from api.user.handler import UserHandlerApi, UserListHandlerApi
from conf.constant import prefix_api

urlpatterns = [
    url(r'^/{}/user/management'.format(prefix_api), UserHandlerApi),  # 用户管理
    url(r'^/{}/user/management/(?P<user_id>\d+)'.format(prefix_api), UserHandlerApi),  # 用户删除
    url(r'^/{}/user/list'.format(prefix_api), UserListHandlerApi),  # 用户列表
]
