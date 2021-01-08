# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# import asyncio
#
# from aio_pika import connect_robust
# import aio_pika
# from loguru import logger
# from conf.constant import ws_rabbitmq
#
# QUEUE = asyncio.Queue()
#
# HOST, PORT, USER, PWD, VIRTUAL_HOST = ws_rabbitmq["host"], ws_rabbitmq["port"], ws_rabbitmq["user"], ws_rabbitmq["password"], \
#                                       ws_rabbitmq["vhost"]
#
#
# async def _init_with_mq_loop(loop):
#     """
#     rabbitmq 连接池
#     :param loop: 循环
#     :return: mq pool
#     """
#     __pool = await connect_robust(loop=loop, host=HOST, login=USER, password=PWD, virtualhost=VIRTUAL_HOST, port=PORT)
#     return __pool
#
#
# class RabbitMQPool(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             logger.debug("init rabbitmq pool")
#             _loop = kwargs.get("loop", None)
#             assert _loop, "use get_event_loop()"
#             cls._rabbitmq = _loop.run_until_complete(_init_with_mq_loop(_loop))
#             cls._instance = super(RabbitMQPool, cls).__new__(cls)
#         return cls._instance
#
#     def get_conn(self) -> aio_pika.Connection:
#         return self._rabbitmq
