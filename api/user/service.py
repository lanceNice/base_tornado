#!/usr/bin/env python
# -*- coding:utf-8 -*-

from api.base.service import BaseService
from api.user.model import User
from conf import page, max_per_page, current_page
from db.mysql_transaction import Transaction
from tools.logger import logger
from tools.response import Code


class UserService(BaseService):
    model = User

    @Transaction.transaction
    async def user_create(self, **kwargs):
        """
        新增用户
        :param kwargs:
        :return:
        """
        res = None
        try:
            code = Code.SUCCEED
            phone = kwargs.get("phone", "")
            if not phone:
                return res, Code.PARAM_VALIDATE_FAIL

            user = await self.find_one(phone=phone)
            if user:
                return res, Code.USER_EXIST
            user_dict = {
                "phone": phone,
                "password": "112321",
                "type": 1
            }
            await self.insert(**user_dict)

        except Exception as e:
            code = Code.ERROR
            logger.error(str(e))
        return res, code

    @Transaction.transaction
    async def user_update(self, **kwargs):
        """
        更新用户
        :param kwargs:
        :return:
        """
        res = None
        try:
            code = Code.SUCCEED
            phone = kwargs.get("phone", None)
            password = kwargs.get("password", None)
            user = await self.find_one(phone=phone)
            if not user:
                return res, Code.USER_NOT_EXIST
            user.password = password
            await self.update(user)
        except Exception as e:
            code = Code.ERROR
            logger.error(str(e))
        return res, code

    @Transaction.transaction
    async def user_delete(self, user_id=None):
        res = None
        try:
            code = Code.SUCCEED
            if not user_id:
                return res, Code.USER_NOT_EXIST
            user = await self.find_one(id=user_id)
            if not user:
                return res, Code.USER_NOT_EXIST
            await self.delete(user)
        except Exception as e:
            code = Code.ERROR
            logger.error(str(e))
        return res, code

    async def user_list(self, **kwargs):
        res = None
        try:

            # redis使用
            # await self.redis.set("lance", "sdsadasd")
            # print(await self.redis.get("lance"))

            code = Code.SUCCEED
            phone = kwargs.get("phone", "")
            page_num = kwargs.get("page_num", current_page)
            offset = kwargs.get("offset", max_per_page)

            args = ("id", "phone")
            kwargs = {
                "phone": phone,
                "order_by": {
                    "create_time": "desc"
                },
                "contains": ["phone"],
                "page": page_num,
                "offset": offset,
                "status": 1
            }

            result = await self.enhance_find(*args, **kwargs)
            count = await self.enhance_find_count(**kwargs)
            res = {
                "result": result,
                "count": count
            }
        except Exception as e:
            code = Code.ERROR
            logger.error(str(e))
        return res, code
