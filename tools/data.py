# -*- coding: utf-8 -*-
# 数据操作工具类
from functools import reduce


def list_of_multi(str_data) -> int:
    if isinstance(str_data, str):
        nums = str_data.split("*")
        int_num = [int(num) for num in nums]
        result = reduce(lambda x, y: x * y, int_num)
    else:
        result = str_data
    return result
