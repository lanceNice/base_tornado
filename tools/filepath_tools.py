# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 16:18
# @Author  : lance
# @File    : file_utils.py
# @Software: PyCharm
# 文件路径工具
import os


def get_conf_file_path(filename):
    """
    得到conf文件夹下的文件路径
    :param filename: 文件名称
    :return:
    """
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    database_path = base_dir + '/conf/'
    return database_path + filename
