#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

# 判断是开发环境,测试环境,正式环境，分别用 dev, test, prod来表示，默认就是测试环境
profile = os.getenv("profile", "test")
