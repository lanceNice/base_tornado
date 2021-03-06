#!/usr/bin/env python
# -*- coding:utf-8 -*-


import aioredis
from conf.constant import redis as _redis
from tools.logger import logger


async def _init_with_loop(loop):
    """
    redis 连接池
    :param loop: 循环
    :return: redis pool
    """
    address = 'redis://%s' % _redis["host"]
    password = _redis["password"]
    __pool = await aioredis.create_redis_pool(
        address, minsize=5, maxsize=_redis["max_connections"], encoding='utf8', password=password, loop=loop,
        db=_redis["db"]
    )
    return __pool


class RedisPool(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            logger.debug("init redis pool")
            _loop = kwargs.get("loop", None)
            assert _loop, "use get_event_loop()"
            cls._redis = _loop.run_until_complete(_init_with_loop(_loop))
            cls._instance = super(RedisPool, cls).__new__(cls)
        return cls._instance

    def get_conn(self) -> aioredis.Redis:
        return self._redis
