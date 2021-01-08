#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 基础工具


def get_dict_args(*args, **kwargs):
    """
    删除字典中值为空的数据，排除特殊字段
    :param kwargs:
    :return:
    """
    _dict = {}
    for key, val in kwargs.items():

        if key in args:
            _dict[key] = val
    return _dict


def delete_dict(*args, **kwargs):
    """
    删除字典中指定的key
    :param args:
    :param kwargs:
    :return:
    """
    for key in list(kwargs.keys()):
        if key in args:
            del kwargs[key]
    return kwargs


if __name__ == '__main__':
    pass
