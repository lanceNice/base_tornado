#!/usr/bin/env python
# -*- coding:utf-8 -*-
from apscheduler.schedulers.tornado import TornadoScheduler

scheduler = TornadoScheduler(timezone="Asia/Shanghai")


# 设置为每日凌晨00:01:01时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='1', minute='1', second='0')
def rebate():
    pass


# 设置每30秒更新
@scheduler.scheduled_job('interval', seconds=30)
def rebate_company():
    pass


# 设置为每日凌晨02:01:00时执行一次调度程序
@scheduler.scheduled_job("cron", day_of_week='*', hour='2', minute='1', second='0')
async def update_city():
    pass
