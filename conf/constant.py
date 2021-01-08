#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tools.list_transfer_num import list_of_multi
from tools.parse_yaml import ParseYaml

import os

# 判断是开发环境,测试环境,正式环境，分别用 dev, test, prod来表示，默认就是测试环境
profile = os.getenv("profile", "test")

parse_yaml = ParseYaml().instance(profile)

# ################ yaml 配置 ###################

# 数据库读写分离的
write_mysql = parse_yaml.parse(section="write_mysql")
read_mysql = parse_yaml.parse(section="read_mysql")

# 默认头部信息
prefix_info = parse_yaml.app_parse(section="prefix_info")
prefix_db = prefix_info.get("prefix_db")
prefix_api = prefix_info.get("prefix_api")

# session 配置
session = parse_yaml.app_parse(section="session")
secret_key = session.get("secret_key")
_jwt_expire = session.get("jwt_expire")
access_token_time = list_of_multi(_jwt_expire)
_refresh_token = session.get("refresh_token")
refresh_token_time = list_of_multi(_refresh_token)

# sms 配置
sms = parse_yaml.app_parse(section="sms")
appid = sms.get("appid")
appkey = sms.get("appkey")
sign = sms.get("sign")
template_id = sms.get("template_id")
valid_time = sms.get("valid_time")

# redis
redis = parse_yaml.parse(section='redis')

# rabbitmq
rabbitmq = parse_yaml.parse(section='rabbitmq')

# 分页配置
page = parse_yaml.parse(section="page")
current_page = page.get("current_page", 1)
max_per_page = page.get("max_per_page", 10)

# 主url配置
site_url = parse_yaml.parse(section="site_url")
host_url = site_url.get("url")

#  图片路径存放地址
pic_path = parse_yaml.parse(section='pic_path')
path = pic_path.get("path")

# app应用的端口以及ip
app = parse_yaml.parse(section="app")
address = app.get("address", "127.0.0.1")
port = app.get("port", "8080")

# 日志解析
log = parse_yaml.parse(section="log")
log_path = log.get("log_path")
log_level = log.get("log_level")

# todo ############ 普通常量（不在yaml中配置的直接在下面添加即可） ####################
