#!/usr/bin/env python
# -*- coding:utf-8 -*-
from conf.constant import secret_key,host_url, max_per_page, redis, rabbitmq

settings = {
    "secret_key": secret_key,
    "site_url": host_url,
    'max_per_page': max_per_page,
    'paginate_param': 'page',
    'redis': redis,
    'rabbitmq': rabbitmq
}
