#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import random

from qcloudsms_py import SmsSingleSender
from conf.constant import appid, appkey, sign, template_id, valid_time
from tools import Code
from tools.logger import logger


def get_sws_code(phone):
    """
    短信验证码
    文档： # https://cloud.tencent.com/document/product/382/5976
    # NOTE: 真实的签名需要在短信控制台中申请，另外签名参数使用的是`签名内容`，而不是`签名ID`
    :param phone: 手机号
    :return:
    """
    try:
        # 短信应用SDK AppKey
        # 需要发送短信的手机号码
        phone_numbers = [phone]
        ssender = SmsSingleSender(appid, appkey)
        random_code = random.randint(100000, 999999)
        params = [random_code]
        result = ssender.send_with_param(86, phone_numbers[0], template_id, params, sign=sign, extend="",
                                         ext="")  # 签名参数未提供或者为空时，会使用默认签名发送短信
        if result and result['result'] == 0:
            # 获取短信成功
            return Code.SUCCEED, random_code
        elif result and result['result'] == 1025:
            return Code.SMS_LIMIT, Code.Msg.get("SMS_LIMIT")
        elif result and result["result"] == 1014:
            return Code.SMS_TEMPLATE_ERROR, Code.Msg.get("SMS_TEMPLATE_ERROR")
        elif result and result["result"] == 1001:
            return Code.ERROR, "sig 签名错误"
        else:
            # 获取短信失败
            return result["result"], result["errmsg"]
    except Exception as e:
        logger.error(e)
        return Code.SMS_FAILED, Code.Msg.get("SERVER_ERROR")


if __name__ == '__main__':
    code, res = get_sws_code("15738854260")
    print(res, code)
