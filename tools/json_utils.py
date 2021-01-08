# -*- coding: utf-8 -*-
# @Time    : 2019/12/24 15:16
# @Author  : lance
# @File    : json_utils.py
# @Software: PyCharm

import json


def read(file_path):
    """
    json 文件读取
    :param file_path:
    :return:
    """
    with open(file_path, 'rb') as f:
        res_list = json.load(f)
    return res_list


def write(file_path, text):
    """
    json 文件写入
    :param file_path:
    :param text:
    :return:
    """
    file = open(file_path, "wb")
    file.write(text.encode("utf-8"))


if __name__ == '__main__':
    # file_path = "mycity.json"
    # import requests
    # text = requests.get("https://hzbj.yooticloud.cn/yzg/db/list").text
    # print(write(file_path, text))
    pass
