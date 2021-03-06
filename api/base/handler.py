#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

import redis
from abc import ABC
from typing import Any

from tornado.escape import json_decode, to_unicode
from tornado.web import RequestHandler, MissingArgumentError
from tools.response import Code, res


class BaseHandler(RequestHandler, ABC):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

    def get(self, *args):
        self.write_error(404)

    def post(self, *args):
        self.write_error(404)

    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Headers', '*')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Content-type', 'application/json')
        self.set_header('Access-Control-Allow-Credentials', "true")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, DELETE, PUT, PATCH, OPTIONS')
        self.set_header('Access-Control-Allow-Headers',
                        'Content-Type, Authorization, Access-Control-Allow-Origin, Access-Control-Allow-Headers, '
                        'X-Requested-By, Access-Control-Allow-Methods')

    def get_json_argument(self, name, default=None):
        args = json_decode(self.request.body)
        name = to_unicode(name)
        if name in args:
            return args.get(name)
        elif default is not None:
            return default
        else:
            raise MissingArgumentError(name)

    # 获取请求数据字典
    def get_request_dict(self, key_list):
        res_dict = {}
        for key in key_list:
            res_dict.update({key: self.get_json_argument(key, "")})
        return res_dict

    def write_error(self, status_code: int, **kwargs: Any):
        try:
            if status_code == Code.Msg.get("URL_NOT_FOUND"):
                error_msg = "请求的api不存在!"
            else:
                msg = kwargs.get("exc_info")[1]
                if hasattr(msg, "log_message"):
                    error_msg = kwargs.get("exc_info")[1].log_message
                else:
                    error_msg = kwargs.get("exc_info")[1].args[0]
                    error_msg = "Key %s is not exist!" % error_msg
        except MissingArgumentError as e:
            error_msg = str(e)
        except KeyError as e:
            error_msg = str(e)
        except TypeError as e:
            error_msg = str(e)
        except Exception as e:
            error_msg = str(e)
        result = res(code=status_code, msg=error_msg)
        return self.finish(result)

    def response(self, code=Code.SUCCEED, msg=None, data=None):
        """统一返回消息"""
        self.write(res(code=code, msg=msg, data=data))
