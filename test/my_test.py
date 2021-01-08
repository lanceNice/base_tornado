# -*- coding: utf-8 -*-
# @Time    : 2021/1/6 10:48
# @Author  : lance
# @File    : my_test.py
# @Software: PyCharm
from databases import WriteMysqlPool, RedisPool


class BaseService(object):


    @property
    def redis(self):
        a=2
        return a


if __name__ == '__main__':
    a= BaseService()
    res=a.redis
    b=1