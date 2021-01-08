#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bcrypt import hashpw, gensalt
from peewee import CharField, IntegerField, BooleanField, BlobField

from api.base.model import BaseModel
from conf.constant import prefix_db


class PasswordHash(bytes):
    def check_password(self, password):
        password = password.encode('utf-8')
        return hashpw(password, self) == self


class PasswordField(BlobField):
    def __init__(self, iterations=12, *args, **kwargs):
        if None in (hashpw, gensalt):
            raise ValueError('Missing library required for PasswordField: bcrypt')
        self.bcrypt_iterations = iterations
        super(PasswordField, self).__init__(*args, **kwargs)

    def db_value(self, value):
        """Convert the python value for storage in the database."""
        if isinstance(value, PasswordHash):
            return bytes(value)

        if isinstance(value, str):
            value = value.encode('utf-8')
        salt = gensalt(self.bcrypt_iterations)
        return value if value is None else hashpw(value, salt)

    def python_value(self, value):
        """Convert the database value to a pythonic value."""
        if isinstance(value, str):
            value = value.encode('utf-8')
        return PasswordHash(value)


class User(BaseModel):
    company_name = CharField(null=True, index=True, verbose_name='企业名称')
    company_socialcreditcode = CharField(null=True, max_length=18, index=True, verbose_name='企业社会统一信用代码')
    name = CharField(null=True, max_length=40, index=True, verbose_name="联系人姓名")
    phone = CharField(null=True, max_length=11, index=True, verbose_name="联系人手机号")
    password = PasswordField(verbose_name="密码")
    note = CharField(null=True, verbose_name="备注")
    type = IntegerField(verbose_name="用户类型")  # 1:管理员　2:普通用户
    app_id = CharField(null=True, max_length=40, index=True, verbose_name="应用id")
    app_key = CharField(null=True, max_length=40, index=True, verbose_name="应用key")
    yzg_address = CharField(null=True, verbose_name="云住工地址")
    yzg_user = CharField(null=True, verbose_name="云住工账号")
    yzg_password = CharField(null=True, verbose_name="云住工账号密码")
    yzg_city_name = CharField(null=True, verbose_name="云住工城市名字")
    yzg_city_db = CharField(null=True, verbose_name="云住工城市库名")

    class Meta:
        table_name = prefix_db + "user"
