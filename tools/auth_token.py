#!/usr/bin/env python
# -*- coding:utf-8 -*-
# token 相关
import datetime
import json
import jwt
from conf.constant import refresh_token_time, access_token_time, secret_key
from tools import res, Code
from tools.logger import logger


def encode_auth_token(user_id, token_name='access_token'):
    """
    生成认证Token
    """
    delta = datetime.timedelta(days=refresh_token_time) if token_name == 'refresh_token' else \
        datetime.timedelta(seconds=access_token_time)
    exp_time = datetime.datetime.utcnow() + delta

    try:
        payload = {
            'exp': exp_time,
            'iat': datetime.datetime.utcnow(),
            'data': {
                'token_name': token_name,
                'id': user_id
            }
        }
        return jwt.encode(
            payload,
            secret_key,
            algorithm='HS256',
        ).decode('utf-8')  # 将bytes转化为str
    except Exception as e:
        logger.info(str(e))


def decode_auth_token(auth_token):
    """
    验证Token
    :param auth_token:
    :return: integer|string
    try:
         payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'), leeway=datetime.timedelta(seconds=10))
        # 取消过期时间验证
        payload = jwt.decode(token, SECRET_KEY, options={'verify_exp': False}, algorithms=['HS256'])
        print(payload)
        if 'data' in payload and 'id' in payload.get['data']:
            return payload
        else:
            raise jwt.InvalidTokenError
    except jwt.ExpiredSignatureError:
        return 'Token过期'
    except jwt.InvalidTokenError:
        return '无效Token'
        """
    try:
        payload = jwt.decode(
            auth_token,
            secret_key,
            algorithms=['HS256'],
            options={"verify_exp": True}
        )
        return res(code=Code.SUCCEED, data=payload.get('data'))
    except jwt.ExpiredSignatureError:
        return res(code=Code.SESSION_EXPIRED, msg="登录过期！")  # token过期，自动重发token
    except jwt.InvalidTokenError:
        return res(code=Code.SESSION_ERROR, msg="TOKEN 无效！")  # token错误, 需要重新登录


def generate_new_token(self):
    refresh_token = self.request.headers.get('refresh_token', None)
    _res = decode_auth_token(refresh_token)
    _res = json.loads(_res)
    if _res["code"] == Code.SUCCEED:
        return encode_auth_token(_res["data"]['id'])
    else:
        return None


if __name__ == '__main__':
    print(encode_auth_token(1))
    print(decode_auth_token(
        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2MDkyMzA1NzEsImlhdCI6MTYwNzkzNDU3MSwiZGF0YSI6eyJ0b2tlbl9uYW1lIjoiYWNjZXNzX3Rva2VuIiwiaWQiOjF9fQ.oYRhDvykmFDo5SXZOqssQdLwiWms3AeAm7_p3wcwQek"))
