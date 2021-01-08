#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from conf.constant import path as _path


def remove_file(name):
    """
    移除指定的文件
    :param name:
    :return:
    """
    path = _path + "/%s" % name
    if os.path.exists(path):
        os.remove(path)


def dir_is_exist(path):
    """
    判断文件夹是否存在
    :param path:
    :return:
    """
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)

