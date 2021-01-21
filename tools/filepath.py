# -*- coding: utf-8 -*-
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


if __name__ == '__main__':
    print(get_conf_file_path("city.json"))
