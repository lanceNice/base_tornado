#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import random
import string
import time
import uuid


def generate_random_str(random_length=8):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'abcdefghigklmnopqrstuvwxyz'
    # base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


def generate_not_repeat_str(random_length=8):
    value = "".join([random.choice(string.ascii_lowercase) for _ in range(random_length)])
    return value


def only_guid(length=18):
    """
    生成全局唯一的guid　根据指定长度来动态计算时间戳的长度，时间戳长度不足指定长度时，进行随机数补齐
    :param length: 指定长度
    :return:
    """
    md5 = hashlib.md5()
    app_id = str(time.time() * 1000 * 100).replace('.', '')
    if len(app_id) > length:
        app_id = app_id[:length]
    else:
        add = length - len(app_id) % length if len(app_id) % length else 0
        app_id += ''.join(random.sample(string.ascii_letters, add))
    data = app_id.encode("utf-8")
    md5.update(data)
    return md5.hexdigest()


def generate_uuid4_str():
    uuid4 = str(uuid.uuid4())
    _uuid4 = uuid4.replace("-", "")
    return _uuid4


if __name__ == '__main__':
    # print(generate_random_str())
    # print(generate_not_repeat_str())
    print(generate_uuid4_str())
