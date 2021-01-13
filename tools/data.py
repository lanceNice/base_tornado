# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 17:26
# @Author  : lance
# @File    : data_tools.py
# @Software: PyCharm
from functools import reduce


def list_of_multi(str_data) -> int:
    if isinstance(str_data, str):
        nums = str_data.split("*")
        int_num = [int(num) for num in nums]
        result = reduce(lambda x, y: x*y, int_num)
    else:
        result = str_data
    return result
