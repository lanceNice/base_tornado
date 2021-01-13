#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio
import platform

from tornado import web
from tornado.httpserver import HTTPServer
import scheduler_task
from api import urlpatterns
from conf.constant import address, port, profile
from db import RedisPool, ReadMysqlPool, WriteMysqlPool
from tools.logger import logger

scheduler = scheduler_task.scheduler


def make_app(_loop):
    if profile != "prod":
        debug = True
    else:
        debug = False

    # 启动配置
    settings = {
        "debug": debug
    }

    apps = web.Application(
        urlpatterns,
        **settings
    )
    # 需要事件循环,初始化redis连接池
    apps.redis_pool = RedisPool(loop=_loop)
    # 初始化数据库连接池
    apps.read_mysql_pool = ReadMysqlPool()
    apps.write_mysql_pool = WriteMysqlPool()
    return apps


def main():
    try:

        logger.info("server start: http://{}:{}".format(address, port))
        loop = asyncio.get_event_loop()
        app = make_app(loop)
        app.listen(address=address, port=port)
        # 多进程启动，设置body大小
        server = HTTPServer(app, max_buffer_size=1009715200, max_body_size=1009715200)
        if platform.system() == 'Windows':
            logger.info("server system:{}".format("Windows"))

        elif platform.system() == 'Linux':
            server.start(9)  # Forks multiple sub-processe  2n+1
            logger.info("server system:{}".format("Linux"))

        # 开启定时器
        if profile == "prod" or profile == "dev":
            scheduler.start()
        # 开启事件循环
        loop.run_forever()

    except KeyboardInterrupt:
        logger.info("\nStop the service")


if __name__ == '__main__':
    main()
