#!/usr/bin/env python
# -*- coding:utf-8 -*-
from peewee_async import PooledMySQLDatabase
from conf.constant import write_mysql
from playhouse.migrate import *
from conf.constant import prefix_db
from api.user.model import User
from api.record.model import Record

my_db = PooledMySQLDatabase(
    write_mysql['db'],
    host=write_mysql['host'],
    port=write_mysql['port'],
    user=write_mysql['user'],
    password=write_mysql['password']
)

migrator = PostgresqlMigrator(my_db)


def init_table():
    tables = [User,Record]
    for table in tables:
        my_db.create_tables([table])


"""
   添加：指定表名，列名，表定义    
    migrator.add_column('table_name', 'pub_date', pubdate_field),
    migrator.add_column('table_name', 'comment', comment_field),
 
    # 删除： 指定表名，列名
    migrator.drop_column('story', 'some_old_field'),
 
    # 重命名列：指定表名，列名，新列名
    migrator.rename_column('story', 'mod_date', 'modified_date'),
 
    # 设置允许空或不允许空：表名，列名
    migrator.drop_not_null('story', 'pub_date'),      # 允许为空
    migrator.add_not_null('story', 'modified_date'),      # 非空
 
    # 重命名表：指定表名，新表名    
    migrator.rename_table('story', 'stories_tbl'),
 
    # 添加索引：表名，列名（集合），是否唯一
    migrator.add_index('story', ('pub_date',), False),    # 添加pub_date列索引，不唯一
    migrator.add_index('story', ('category_id', 'title'), True),    # 添加category_id, title 索引， 唯一
 
    # 删除索引： 表明，列名
    migrator.drop_index('story', 'story_pub_date_status')

"""


def add_field(table_name, column_name, field_name):
    """
    添加表下,对应的列名以及字段名
    :param table_name: 表名
    :param column_name: 列名
    :param field_name: 字段名
    :return:
    """
    try:
        migrate(
            migrator.add_column(prefix_db + table_name, column_name, field_name)
        )
    except ProgrammingError as e:
        print("add_field, ProgrammingError: " + e.args[0])
    except Exception as e:
        print("add_field, Exception: " + e.args[0])


def delete_field(table_name, column_name):
    """
    删除表下对应的列名
    :param table_name: 表名
    :param column_name: 列名
    :return:
    """
    try:
        migrate(
            migrator.drop_column(prefix_db + table_name, column_name),
        )
    except ProgrammingError as e:
        print("delete_field, ProgrammingError: " + e.args[0])
    except Exception as e:
        print("delete_field, Exception: " + e.args[0])


def update_table_add_field():
    # todo 新增的字段, 当调用完成后, 一定删除当下新增的字段,否则下次新增会提示字段已存在
    _test = IntegerField(default=0, verbose_name='测试', help_text='测试')
    add_field("category", "test", _test)


def update_table_delete_field():
    # todo 删除字段时, 当调用完成后, 一定删除字段名称,否则下次新增会提示字段不存在存在
    delete_field("category", "test")


if __name__ == '__main__':
    init_table()
    # update_table_add_field()
    # update_table_delete_field()
