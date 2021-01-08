#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
import itertools
import json
from functools import wraps

from api.exception import ApiHTTPError
from api.user.service import UserService
from tools import Code
from tools.auth_token import decode_auth_token, encode_auth_token
from tools.logger import logger


class Row(dict):
    """A dict that allows for object-like property access syntax."""

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


def set_dict(data) -> Row:
    return Row(itertools.zip_longest(data.keys(), data.values()))


# 异步装饰器
def authenticated_async():
    def decorator(func):
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            try:
                authorization = self.request.headers.get(
                    'Authorization', None
                )
                if not authorization:
                    self.response(code=Code.TOKEN_MUST_ADD)
                    return await self.finish()
                authorization = authorization.split(' ')
                if len(authorization) != 2:
                    self.response(code=Code.TOKEN_FORMAT_ERROR)
                    return await self.finish()
                else:
                    if authorization[0] != 'YTC':
                        self.response(code=Code.TOKEN_FORMAT_ERROR)
                        return await self.finish()
            except Exception as e:
                logger.info("解析token异常： " + str(e))
                # raise ForbiddenError()
            else:
                authorization = authorization[1]
                if authorization:
                    try:
                        res = decode_auth_token(authorization)  # 解出来code=1就表明token正确
                        res = json.loads(res)
                        if res.get("code", "") == Code.SUCCEED and 'data' in res:
                            return await func(self, *args, **kwargs)
                        else:
                            self.response(code=res['code'])
                            return await self.finish()
                    except Exception as e:
                        print("error----------------  " + str(e))
                        logger.info("解码token异常: " + str(e))
                        raise ApiHTTPError(status_code=500, log_message="响应异常")

        return wrapper

    return decorator


def log(content):
    """
    记录数据库审计日志
    :param content: 操作内容
    :return:
    """

    def logger_(func):
        # 添加了字典对应的参数
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            log_kwargs = {
                "user_id": self.current_user.id if self.current_user else 0,
                "content": content
            }
            # res, code = await AuditLogService.instance().create_log(**log_kwargs)
            result = await func(self, *args, **kwargs)
            print(result, func, self.request.body)
            return result

        return wrapper

    return logger_


def record_http_request(func):
    """
    @function 用于记录每个http请求
    """

    @wraps(func)
    def record(self, *args, **kwargs):
        request_time = str(datetime.now())
        response = func(self, *args, **kwargs)
        http_request = dict(
            request_time=request_time,
            expend_time=self.request.request_time(),
            response_time=str(datetime.now()),
            request_ip=self.request.remote_ip,
            method=self.request.method,
            url=self.request.uri,
            request_params=self.request.arguments,
            response_code=self.get_status(),
            response_text=self.response_value,
        )
        return response

    return record
