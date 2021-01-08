#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 时间相关工具类
from datetime import timedelta, datetime
import arrow as arrow


# 计时装饰器
def count_time():
    def tmp(func):
        def wrapped(*args, **kwargs):
            start_time = datetime.now()  # 程序开始时间
            result = func(*args, **kwargs)
            over_time = datetime.now()  # 程序结束时间
            total_time = (over_time - start_time).total_seconds()
            print('程序共计%s秒' % total_time)
            print('%s called cost time : %s' % (func.__name__, total_time))
            return result

        return wrapped

    return tmp


# 日期相关
class Date(object):

    # 加八小时处理
    @classmethod
    def add_8hours(cls, time):
        """
        :param time:
                type:datetime
                format:'%Y-%m-%d %H:%M:%S'
        :return: unicode
        """

        if not isinstance(time, type(datetime.utcnow())):
            return ''
        return (time + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')

    # 减八小时处理
    @classmethod
    def sub_8hours(cls, time):
        """
        :param time
                    type:datetime
                    format:'%Y-%m-%d %H:%M:%S'
        :return: unicode
        """
        if not isinstance(time, type(datetime.utcnow())):
            return ''
        return (time - timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')

    @classmethod
    def now(cls):
        """
        :return: datetime
        """
        return datetime.utcnow() + timedelta(hours=8)

    # 获取当前北京时间
    @classmethod
    def get_now_time(cls):
        return Date.now().strftime('%Y-%m-%d %H:%M:%S')

    # 获取当前北京日期
    @classmethod
    def today(cls):
        return Date.now().strftime('%Y-%m-%d')

    # 获取当前北京月
    @classmethod
    def month(cls):
        return Date.now().strftime('%Y-%m')

    # 获取当前上一个月份
    @classmethod
    def last_month(cls):
        _now = arrow.now()
        return _now.shift(months=-1).format("YYYY-MM")

    # 获取距当前指定小时的时间戳
    @classmethod
    def get_specify_hours_time(cls, hours=12):
        _now = arrow.now() + timedelta(hours=hours)
        seconds = _now.timestamp
        return seconds

    # 转化datetime.time为字符串
    @classmethod
    def transfer_date_to_str(cls, _date):
        """
        :param _date:
        :return:
        """
        return _date.strftime('%H:%M:%S')


# 获取日期列表(天)
def get_date_list(start_date, end_date):  # end_date=None
    """
    :param start: 开始日期 2020-12-10
    :param end: 结束日期 2020-12-20
    :return:
    """
    if start_date is not None:
        start = datetime.strptime(start_date, "%Y-%m-%d")
    if end_date is None:
        end = datetime.now()
    else:
        end = datetime.strptime(end_date, "%Y-%m-%d")
    data = []

    def gen_dates(b_date, days):
        day = timedelta(days=1)
        for i in range(days):
            yield b_date + day * i

    for d in gen_dates(start, ((end - start).days + 1)):  # 29 + 1
        data.append(d.strftime("%Y-%m-%d"))
    return data


# 获取日期列表（时）
def get_hour_list(start_date, end_date):  # end_date=None
    """
    :param start: 开始时间 2018-03-01 00
    :param end: 结束时间 2018-03-01 00
    :return:
    """

    timestamp_format = '%Y-%m-%d %H'
    ts_obj = datetime.strptime(start_date, timestamp_format)
    latest_ts_obj = datetime.strptime(end_date, timestamp_format)
    ts_raw = []
    while ts_obj <= latest_ts_obj:
        ts_raw.append(ts_obj)
        ts_obj += timedelta(hours=1)

    dates_formatted = [d.strftime('%Y-%m-%d %H') for d in ts_raw]
    return dates_formatted


# 获取月份列表（月）
def get_month_list(start_date, end_date):
    """
    @param start_date:开始日期 2020-12-10
    @param end_date: 结束日期 2020-12-20
    @return:
    """
    dates = get_date_list(start_date, end_date)
    months = []
    for i in dates:
        if i[:7] not in months:
            months.append(i[:7])
    return months


if __name__ == '__main__':
    print(Date.get_specify_hours_time(hours=0))
