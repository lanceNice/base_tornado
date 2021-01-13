#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from peewee import Model, PrimaryKeyField, BooleanField, DateTimeField
from db import WriteMysqlPool


# Model 基类
class BaseModel(Model):
    id = PrimaryKeyField(unique=True, index=True, verbose_name="主键", help_text='主键')
    create_time = DateTimeField(default=datetime.now, index=True, verbose_name="新增本地时间", help_text='新增本地时间')
    update_time = DateTimeField(default=datetime.now, index=True, verbose_name='更新时间', help_text='更新时间')
    status = BooleanField(default=True, index=True, verbose_name="是否有效,True标识有效,False标识无效")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self._get_pk_value() is None:
            self.create_time = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S")
        self.update_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S")
        return super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        database = WriteMysqlPool().get_conn
