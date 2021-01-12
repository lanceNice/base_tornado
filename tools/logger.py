#!/usr/bin/env python
# -*- coding:utf-8 -*-
# logger 工具类

import logging
import logging.config
import os
import yaml

from tools.file_tools import dir_is_exist
from conf.constant import log_path, log_level


# logger等级获取
def log_parse_level(level=log_level):
    if level == "DEBUG":
        _level = logging.DEBUG
    elif level == "INFO":
        _level = logging.INFO
    elif level == "WARNING":
        _level = logging.WARNING
    elif level == "ERROR":
        _level = logging.ERROR
    elif level == "CRITICAL":
        _level = logging.CRITICAL
    else:
        _level = logging.NOTSET
    return _level


# logger 配置
def setup_logging(default_path="conf/logging.yaml", default_level=log_parse_level(), env_key="LOG_CFG"):
    """
    配置日志的基本信息
    :param default_path: 日志配置文件路径
    :param default_level: 日志级别
    :param env_key: 根据环境变量设置日志的配置文件
    :return:
    """
    dir_is_exist(log_path)
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            logging_config = yaml.safe_load(f)
            info_file_handler_name = logging_config['handlers']['info_file_handler']['filename']
            error_file_handler = logging_config['handlers']['error_file_handler']['filename']
            logging_config['handlers']['info_file_handler']['filename'] = log_path + "/" + info_file_handler_name
            logging_config['handlers']['error_file_handler']['filename'] = log_path + "/" + error_file_handler
            logging.config.dictConfig(logging_config)
    else:
        file_name = log_path + '/record.log'
        logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                            filename=file_name, filemode='a', level=default_level)


# 获取指定logger
def get_logger(name):
    setup_logging()
    _logger = logging.getLogger(name)
    return _logger


logger = get_logger(name="fileLogger")
