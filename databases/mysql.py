#!/usr/bin/env python
# -*- coding:utf-8 -*-
import traceback
from peewee_async import Manager
from peewee_async import PooledMySQLDatabase
from conf.constant import read_mysql as read_mysql_db
from conf.constant import write_mysql as write_mysql_db

from tools.logger import logger


class ReadMysqlPool(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            logger.debug("init read mysql pool")
            cls.conn = PooledMySQLDatabase(
                read_mysql_db['db'],
                host=read_mysql_db['host'],
                port=read_mysql_db['port'],
                user=read_mysql_db['user'],
                password=str(read_mysql_db['password']),
                min_connections=read_mysql_db['min_connections'],
                max_connections=read_mysql_db['max_connections'],
                charset='utf8mb4'
            )
            cls.manager = Manager(cls.conn)
            # todo set_allow_sync False设置异步,True设置同步 异步读数据库管理
            cls.conn.set_allow_sync(False)
            cls._instance = super(ReadMysqlPool, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def get_conn(self):
        return self.conn

    @property
    def get_manager(self):
        return self.manager


class WriteMysqlPool(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            logger.debug("init write mysql pool")
            cls.conn = PooledMySQLDatabase(
                write_mysql_db['db'],
                host=write_mysql_db['host'],
                port=write_mysql_db['port'],
                user=write_mysql_db['user'],
                password=str(write_mysql_db["password"]),
                min_connections=write_mysql_db['min_connections'],
                max_connections=write_mysql_db['max_connections']
            )
            cls.manager = Manager(cls.conn)
            # todo 新增表只能是异步模式
            # cls.conn.set_allow_sync(False)
            cls._instance = super(WriteMysqlPool, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    @property
    def get_conn(self):
        return self.conn

    @property
    def get_manager(self):
        return self.manager
