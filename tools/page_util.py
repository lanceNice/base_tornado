#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime, date

from conf import settings


def json_serial(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError("Type {}s not serializable".format(obj))


def get_page(count):
    """
     获取分页信息
    :param count: 总数
    :return: 总页数
    """
    max_pre_page = settings['max_per_page']
    page = 1
    if count > max_pre_page:
        page = count // max_pre_page
        if count % max_pre_page:
            page += 1
    return page


def get_next_pre_page(current_api_path, current_page, page):
    """
    获取上一页和下一页的url
    :param current_api_path: 当前api相对路径
    :param current_page: 当前页码
    :param page: 总页码
    :return: (previous, next)
    """
    previous = None
    _next = None
    err = None
    current_base_url = settings['site_url'] + current_api_path
    param = settings['paginate_param']
    if current_page < page:
        _next = current_base_url + '?{}={}'.format(param, current_page + 1)
        if current_page == 1:
            previous = None
        else:
            previous = current_base_url + '?{}={}'.format(param, current_page - 1)
    elif current_page == page:
        _next = None
        if current_page == 1:
            previous = None
        else:
            previous = current_base_url + '?{}={}'.format(param, current_page - 1)

    else:
        err = '无效页面。'

    return previous, _next, err
