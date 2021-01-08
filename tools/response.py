#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 接口响应工具
import datetime
import decimal
import json


# 结果统一响应序列化
class UniteEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):  # 序列化Decimal类型数据
            data = float("%.1f" % obj)
            return data
        elif isinstance(obj, datetime.datetime):  # 序列化datetime类型数据
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


# 返回代码和描述
class Code(object):
    BAD_REQUEST = 400
    UNANTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404  # 该请求不存在
    REQUEST_METHOD_NOT_ALLOW = 405  # 请求方式不支持

    SERVER_ERROR = 500  # 服务器错误
    BAD_GATEWAY = 502
    SERVICE_UNAVAILBLE = 503
    GATEWAY_TIMEOUT = 504

    SUCCEED = 1  # 成功
    ERROR = -1  # 失败

    # 常量信息
    ERROR_PARAMS = 10100
    PARAM_VALIDATE_FAIL = 10101  # 必要参数校验失败
    PARAM_LIST_FAIL = 10102  # 传入指定接口的参数
    RESPONSE_DATA_ERROR = 10103  # 响应数据异常
    VALIDATE_DATA_ERROR = 10104  # 数据校验失败
    REQUEST_ARGS_NOT_NULL = 10105
    QUERY_NO_RESULT = 10106
    SESSION_EXPIRED = 10110
    SESSION_ERROR = 10111
    TOKEN_MUST_ADD = 10112
    TOKEN_FORMAT_ERROR = 10113
    TOKEN_INVALID = 10114

    # 密码相关的提示信息
    PASSWORD_ERROR = 10120
    NEW_OLD_PASSWORD_MUST_ADD = 10121
    RESET_PASSWORD_TIG = 10122
    PASSWORD_NOT_NULL = 10123
    PASSWORD_FORMAT_ERROR = 10124
    OLD_PWD_VERIFY_ERROR = 10125
    TWICE_PWD_NOT_EQUAL = 10126

    # 短信提示信息
    SMS_TEMPLATE_ERROR = 10200
    SMS_LIMIT = 10201
    SMS_FAILED = 10202
    SMS_ERROR = 10203
    SMG_EXPIRED_TIME = 10204
    SMS_CODE_MUST_ADD = 10205
    SMS_LIMIT_TIG = 10206
    SMS_CODE_ERROR = 10207

    # 用户信息
    USER_NOT_EXIST = 10301
    USER_EXIST = 10302
    USER_ADD_ERROR = 10303
    USER_AUDIT_TIG = 10304
    USER_FORBID_TIG = 10305
    USER_NOT_NULL = 10306
    USER_NOT_AUTH_LOGIN = 10307
    USER_BIND_OPEN_ID_EXIST = 10308

    # 应用错误码
    APP_EXIST = 10401
    APP_NOT_EXIST = 10402
    APP_ID_MUST_ADD = 10403

    # 验证码
    V_CODE_ERROR = 10501

    Msg = {
        BAD_REQUEST: "请求错误！",
        UNANTHORIZED: "当前请求需要用户验证！",
        FORBIDDEN: "禁止访问！",
        NOT_FOUND: "请求的api不存在！",
        REQUEST_METHOD_NOT_ALLOW: "请求方式不支持！",

        SERVER_ERROR: "服务器异常！",
        BAD_GATEWAY: "网关错误！",
        SERVICE_UNAVAILBLE: "服务不可达！",
        GATEWAY_TIMEOUT: "网关超时！",

        SUCCEED: "成功！",
        ERROR: "失败！",

        USER_EXIST: "该用户已存在！",
        USER_NOT_EXIST: "该用户不存在！",
        PASSWORD_ERROR: "密码错误！",

        SESSION_EXPIRED: "登录过期！",
        SESSION_ERROR: "TOKEN 错误",
        TOKEN_MUST_ADD: "TOKEN 必须添加",
        TOKEN_FORMAT_ERROR: "身份认证信息填写不正确，格式为：YTC token。",
        TOKEN_INVALID: "TOKEN 无效！",

        SMS_TEMPLATE_ERROR: "短信模板错误",
        SMS_LIMIT: "手机号日频率限制",
        SMS_ERROR: "获取短信验证码失败",
        SMS_FAILED: "发送短信失败",
        SMG_EXPIRED_TIME: "短信验证码过期",
        SMS_CODE_MUST_ADD: "验证码必须添加",
        SMS_LIMIT_TIG: "发送验证码间隔不能小于5分钟",
        SMS_CODE_ERROR: "短信验证码错误",

        ERROR_PARAMS: "参数错误！",
        PARAM_VALIDATE_FAIL: "参数校验失败！",
        PARAM_LIST_FAIL: "传入指定接口的参数，传入指定外的参数不允许请求接口！",
        QUERY_NO_RESULT: "未查询到结果！",

        RESPONSE_DATA_ERROR: "响应数据异常！",
        VALIDATE_DATA_ERROR: "数据校验失败！",

        REQUEST_ARGS_NOT_NULL: "请求参数不能为空！",

        APP_EXIST: "应用已存在！",
        APP_NOT_EXIST: "应用不存在！",
        APP_ID_MUST_ADD: "应用id必须添加！",

        V_CODE_ERROR: "验证码错误！",
    }


# 响应统一返回
def res(code=Code.SUCCEED, msg=None, data=None) -> str:
    """
    封装的通用返回方法
    :param code: http，返回代码，默认为 1成功
    :param msg: 返回消息，默认为'成功'
    :param count: 数量，默认为0
    :param data:    返回的数据列表，必须是可以iterator，比如dict,list,tuple都可以
    :return json:   返回json对象
    """
    result = dict()
    result['code'] = code
    message = msg if msg else Code.Msg.get(code)
    result['msg'] = message
    if data is not None:
        result['data'] = data
    return json.dumps(result, ensure_ascii=False, cls=UniteEncoder)
