#!/usr/bin/env python
# -*- coding:utf-8 -*-

from functools import reduce


def list_of_multi(str_data) -> int:
    if isinstance(str_data, str):
        nums = str_data.split("*")
        int_num = [int(num) for num in nums]
        result = reduce(lambda x, y: x*y, int_num)
    else:
        result = str_data
    return result


if __name__ == '__main__':
    print(list_of_multi(60))
