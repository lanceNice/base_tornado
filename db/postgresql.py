# #!/usr/bin/env python
# # -*- coding:utf-8 -*-
# # postgresql
# from loguru import logger
# from peewee_async import Manager, PooledPostgresqlDatabase
#
# from conf.constant import write_pg as read_postgresql_db
# from conf.constant import read_pg as write_postgresql_db
#
#
# class ReadPostgreSqlPool(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             logger.debug("init read postgresql pool")
#             cls.conn = PooledPostgresqlDatabase(
#                 read_postgresql_db['db'],
#                 host=read_postgresql_db['host'],
#                 port=read_postgresql_db['port'],
#                 user=read_postgresql_db['user'],
#                 password=str(read_postgresql_db['password']),
#                 min_connections=read_postgresql_db['min_connections'],
#                 max_connections=read_postgresql_db['max_connections']
#             )
#             cls.manager = Manager(cls.conn)
#             # todo set_allow_sync False设置异步,True设置同步 异步读数据库管理
#             cls.conn.set_allow_sync(False)
#             cls._instance = super(ReadPostgreSqlPool, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     @property
#     def get_conn(self):
#         return self.conn
#
#     @property
#     def get_manager(self):
#         return self.manager
#
#
# class WritePostgreSqlPool(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             logger.debug("init write postgresql pool")
#             # PooledPostgresqlDatabase
#             cls.conn = PooledPostgresqlDatabase(
#                 write_postgresql_db['db'],
#                 host=write_postgresql_db['host'],
#                 port=write_postgresql_db['port'],
#                 user=write_postgresql_db['user'],
#                 password=str(write_postgresql_db["password"]),
#                 min_connections=write_postgresql_db['min_connections'],
#                 max_connections=write_postgresql_db['max_connections']
#             )
#             cls.manager = Manager(cls.conn)
#             # todo 新增表只能是异步模式
#             cls.conn.set_allow_sync(False)
#             cls._instance = super(WritePostgreSqlPool, cls).__new__(cls, *args, **kwargs)
#         return cls._instance
#
#     @property
#     def get_conn(self):
#         return self.conn
#
#     @property
#     def get_manager(self):
#         return self.manager
