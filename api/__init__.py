#!/usr/bin/env python
# -*- coding:utf-8 -*-


from tornado.web import url
from api.base.handler import BaseHandler
from api.user import urls as user_urls

# todo 每个文件夹的url对应到本文件夹下进行叠加即可
urlpatterns = user_urls.urlpatterns
urlpatterns.append(url('.*', BaseHandler))
