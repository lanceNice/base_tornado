#!/usr/bin/env python
# -*- coding:utf-8 -*-
from datetime import datetime
from peewee import Model
from playhouse.shortcuts import model_to_dict

from db import RedisPool, ReadMysqlPool, WriteMysqlPool
from tools.base import get_dict_args
from tools.logger import logger
from peewee_async import execute


# service 基类
class BaseService(object):
    model: Model = None
    _service = dict()

    @classmethod
    def instance(cls):
        """Method  instance
        :return: cls
        """
        instance = cls._service.get(cls.__name__, None)
        if not instance:
            instance = cls.__new__(cls)
            cls._service.setdefault(cls.__name__, instance)
        return instance

    # 增
    async def insert(self, **kwargs):
        """保存数据"""
        try:
            return await self.write_mysql_db.create(self.model, **kwargs)
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 改
    async def update(self, obj):
        """更新一条数据"""
        try:
            # 更新数据的修改时间
            obj.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return await self.write_mysql_db.update(obj)
        except self.model.DoesNotExist:
            return None
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 查询一条数据
    async def find_one(self, *args, **kwargs):
        try:
            if not args:
                return await self.read_mysql_db.get(self.model, *args, **kwargs)
            _res = await self.find(*args, **kwargs)
            if len(_res) > 1:
                raise Exception("find multiple data")
            elif len(_res) == 1:
                return _res[0]
            return None
        except self.model.DoesNotExist:
            return None
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 查询多条数据
    async def find(self, *args, **kwargs):
        """查询指定字段，查找多条数据"""
        if not args:
            raise Exception("fields is empty")
        sql = self.model.select(*[getattr(self.model, k) for k in args])
        for key, val in kwargs.items():
            sql = sql.where(getattr(self.model, key) == val)
        try:
            results = await self.read_mysql_db.execute(sql)
            return results
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 增强查询
    async def enhance_find(self, *args, **kwargs):
        results = await self.list_paginate(*args, **kwargs)
        query_data = []
        for res in results:
            data = get_dict_args(*args, **model_to_dict(res))
            query_data.append(data)
        return query_data

    # 增强查询统计
    async def enhance_find_count(self, **kwargs):
        """
        查询总数
        :param kwargs: 查询的条件
        :return:
        """
        sql = self.model.select()

        # 模糊查询 { "no": no,"contains": ["no"]}
        if "contains" in kwargs:
            for contain in kwargs["contains"]:
                if contain in kwargs:
                    sql = sql.where(getattr(self.model, contain).contains(kwargs[contain]))
                    del kwargs[contain]
            del kwargs["contains"]
        # 不等于 {"approve_status": 1,"not_equals": ["approve_status"]}
        if "not_equals" in kwargs:
            for not_equal in kwargs["not_equals"]:
                if not_equal in kwargs:
                    sql = sql.where(getattr(self.model, not_equal) != kwargs[not_equal])
                    del kwargs[not_equal]
            del kwargs["not_equals"]
        # 指定key 不等于 value {"equals_not": {"device_id": None}}
        if "equals_not" in kwargs:
            for key, val in kwargs["equals_not"].items():
                sql = sql.where(getattr(self.model, key) != val)
            del kwargs["equals_not"]
        # 查询in 　field_in = {"type": [1, 2]}
        if "field_in" in kwargs:
            for key, val in kwargs["field_in"].items():
                sql = sql.where(getattr(self.model, key).in_(val))
            del kwargs["field_in"]
        # 查询between {between = {"create_time": [0, 100000000]}}
        if "between" in kwargs:
            for key, val in kwargs["between"].items():
                sql = sql.where(getattr(self.model, key).between(val[0], val[1]))
            del kwargs["between"]
        try:
            for key, val in kwargs.items():
                if key in ('order_by', 'page', 'offset'):
                    continue
                sql = sql.where(getattr(self.model, key) == val)
            count = await self.read_mysql_db.count(sql)
            return count
        except Exception as e:
            logger.exception(str(e))
            raise e

    async def list_paginate(self, *args, **kwargs):
        """
        :param args: 指定返回的字段
        :param kwargs: 查询的条件
        :return:
        """
        if not args:
            raise Exception("fields is empty")
        sql = self.model.select(*[getattr(self.model, k) for k in args])
        # 分页  {"page": 1, "offset": 10}
        if "page" in kwargs and "offset" in kwargs:
            sql = sql.paginate(page=kwargs["page"], paginate_by=kwargs["offset"])
            del kwargs["page"]
            del kwargs["offset"]
        # 排序   {"order_by": {"create_time": "desc"}}
        if "order_by" in kwargs:
            order_by_list = []
            for key, value in kwargs["order_by"].items():
                if value == "desc":
                    order_by_value = -getattr(self.model, key)
                else:
                    order_by_value = getattr(self.model, key)
                order_by_list.append(order_by_value)
            del kwargs["order_by"]
            sql = sql.order_by(*order_by_list).distinct()
        # 模糊查询   { "no": no,"contains": ["no"]}
        if "contains" in kwargs:
            for contain in kwargs["contains"]:
                if contain in kwargs:
                    sql = sql.where(getattr(self.model, contain).contains(kwargs[contain]))
                    del kwargs[contain]
            del kwargs["contains"]
        # 不等于   {"approve_status": 1,"not_equals": ["approve_status"]}
        if "not_equals" in kwargs:
            for not_equal in kwargs["not_equals"]:
                if not_equal in kwargs:
                    sql = sql.where(getattr(self.model, not_equal) != kwargs[not_equal])
                    del kwargs[not_equal]
            del kwargs["not_equals"]
        # 指定key不等于   {"equals_not": {"device_id": None}}
        if "equals_not" in kwargs:
            for key, val in kwargs["equals_not"].items():
                sql = sql.where(getattr(self.model, key) != val)
            del kwargs["equals_not"]
        # 查询in 　field_in = {"type": [1, 2]}
        if "field_in" in kwargs:
            for key, val in kwargs["field_in"].items():
                sql = sql.where(getattr(self.model, key).in_(val))
            del kwargs["field_in"]
        # 查询between {between = {"create_time": [0, 100000000]}}
        if "between" in kwargs:
            for key, val in kwargs["between"].items():
                sql = sql.where(getattr(self.model, key).between(val[0], val[1]))
            del kwargs["between"]
        for key, val in kwargs.items():
            sql = sql.where(getattr(self.model, key) == val)
        try:
            results = await self.read_mysql_db.execute(sql)
            data = [result for result in results]
            return data
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 执行count_sql 直接返回count
    async def custom_sql_query_count(self, sql):
        """
        原生sql查询count
        :param sql:
        :return:
        """
        try:
            count = await self.read_mysql_db.count(sql)
            return count
        except Exception as e:
            logger.exception(str(e))
            raise e

    # 物理删除
    async def delete(self, obj):
        """
        删除， todo 物理删除，根据需求考虑，使用逻辑还是物理删除
        :param obj:
        :return:
        """
        try:
            return await self.write_mysql_db.delete(obj=obj)
        except self.model.DoesNotExist:
            return None
        except Exception as e:
            logger.exception(str(e))
            raise e
            # return None

    # 对象指定值修改
    @classmethod
    async def obj_update(self, obj, data_dicts):
        """
        @param obj: model对象
        @param data_dicts: 需修改的数据 key需要是model的属性 eg：{"name":"yuetian"}
        @return: obj: model对象
        """
        for ind, val in data_dicts.items():
            if val:
                setattr(obj, ind, val)
        return obj

    @staticmethod
    async def execute(sql):
        """执行sql"""
        try:
            return await execute(sql)
        except Exception as e:
            logger.exception(str(e))
            return None

    async def execute_query(self, sql):
        """执行sql"""
        try:
            return await self.read_mysql_db.execute(sql)
        except Exception as e:
            logger.exception(str(e))
            return None

    async def execute_update(self, sql):
        """执行sql"""
        try:
            return await self.write_mysql_db.execute(sql)
        except Exception as e:
            logger.exception(str(e))
            return None

    async def async_execute_fetch_all(self, sql):
        cursor = await self.read_mysql_con.cursor_async()
        await cursor.execute(sql)
        result = await cursor.fetchall()
        result = self.format_result(cursor, result)
        await cursor.release()
        return result

    async def async_execute_update(self, sql):
        cursor = await self.write_mysql_con.cursor_async()
        result = await cursor.execute(sql)
        return result

    @staticmethod
    def format_result(cursor, result):
        """
        原生sql查询结果转dict
        :param cursor: 游标
        :param result: 原生查询结果集
        :return: {}
        """
        return [dict(zip([one[0] for one in cursor.description], row)) for row in result]

    @property
    def read_mysql_db(self):
        return ReadMysqlPool().get_manager

    @property
    def write_mysql_db(self):
        return WriteMysqlPool().get_manager

    @property
    def redis(self):
        return RedisPool().get_conn()

    @property
    def read_mysql_con(self):
        return ReadMysqlPool().get_conn

    @property
    def write_mysql_con(self):
        return WriteMysqlPool().get_conn
