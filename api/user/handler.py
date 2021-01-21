#!/usr/bin/env python
# -*- coding:utf-8 -*-
from abc import ABC

from api.base import authenticated_async
from api.base.handler import BaseHandler
from api.user.service import UserService
from conf import max_per_page, current_page
from tools import Code


class UserHandlerApi(BaseHandler, ABC):

    # @authenticated_async()
    async def post(self):
        """
        用户新增
        """
        kwargs = self.get_request_dict(["phone"])
        res, code = await UserService.instance().user_create(**kwargs)
        if code == Code.SUCCEED:
            self.response(data=res)
        else:
            self.response(code=code, msg=res)
        return await self.finish()

    # @authenticated_async()
    async def put(self):
        """
        用户修改
        :return:
        """
        kwargs = {
            "phone": self.get_json_argument("phone", default=""),
            "password": self.get_json_argument("password", default="")
        }

        res, code = await UserService.instance().user_update(**kwargs)
        if code == Code.SUCCEED:
            self.response(data=res)
        else:
            self.response(code=code, msg=res)
        return await self.finish()

    # @authenticated_async()
    async def delete(self, user_id):
        """
        用户删除
        :return:
        """

        res, code = await UserService.instance().user_delete(user_id=user_id)
        if code == Code.SUCCEED:
            self.response(data=res)
        else:
            self.response(code=code, msg=res)
        return await self.finish()


class UserListHandlerApi(BaseHandler, ABC):

    # @authenticated_async()
    async def post(self):
        """
        用户列表
        """
        kwargs = {
            "phone": self.get_json_argument("phone", default=""),
            "page_num": self.get_json_argument("page_num", current_page),
            "offset": self.get_json_argument("offset", max_per_page)
        }
        res, code = await UserService.instance().user_list(**kwargs)
        if code == Code.SUCCEED:
            self.response(data=res)
        else:
            self.response(code=code, msg=res)
        return await self.finish()
