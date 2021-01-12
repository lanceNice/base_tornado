#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 数据库回滚装饰器
from functools import wraps
from api.base.service import BaseService
from tools.logger import logger
from tools.response import Code


# 使用该装饰器 数据库要设置为显式事务
class Transaction(object):
    @staticmethod
    def transaction(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            db = BaseService().write_mysql_con.atomic_async()
            if db:
                async with db as transaction:
                    result = await func(*args, **kwargs)
                    if result[1] == Code.SUCCEED:
                        await transaction.commit()
                        logger.info('Commit Transaction...')
                    else:
                        logger.warning('Rollback Transaction...')
                        await transaction.rollback()
                    return result
            else:
                return "数据库实例为空！", Code.ERROR

        return wrapper
