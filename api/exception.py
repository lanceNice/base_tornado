#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @File : exception.py 
# @Author: wyg 
# @Date : 2019-07-21 
# @Desc : 重写tornado.web.HTTPError


from tornado.web import HTTPError

from tools.response import Code


class ApiHTTPError(HTTPError):
    def __init__(self, status_code, log_message, *args, **kwargs):
        super(ApiHTTPError, self).__init__(status_code, log_message, *args, **kwargs)


class ForbiddenError(ApiHTTPError):
    def __init__(self, log_message=Code.Msg.get("FORBIDDEN"), status_code=Code.FORBIDDEN, *args, **kwargs):
        super(ForbiddenError, self).__init__(status_code, log_message, *args, **kwargs)


class IllegalError(ApiHTTPError):
    pass


class NotFoundError(ApiHTTPError):
    pass
