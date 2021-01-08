#!/usr/bin/env python
# -*- coding:utf-8 -*-

import aiozipkin as az

from tools.logger import logger

zipkin_address = 'http://127.0.0.1:9411/api/v2/spans'
host, port, service_name = "127.0.0.1", 9411, "attendance_server"


async def _init_with_loop(loop):
    """
    aiozipkin 连接池
    :param loop: 循环
    :return: zipkin pool
    """
    # 设置路由追踪
    endpoint = az.create_endpoint(service_name, ipv4=host, port=port)
    __pool = await az.create(zipkin_address, endpoint, sample_rate=1.0, loop=loop)
    return __pool


class TracerPool(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            logger.debug("init zipkin pool")
            _loop = kwargs.get("loop", None)
            assert _loop, "use get_event_loop()"
            cls._tracer = _loop.run_until_complete(_init_with_loop(_loop))
            cls._instance = super(TracerPool, cls).__new__(cls)
        return cls._instance

    def get_tracer(self):
        return self._tracer
