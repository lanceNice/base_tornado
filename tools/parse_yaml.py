#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import yaml
from conf.profile_env import profile

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATABASE_PATH = base_dir + '/conf/'


class ParseYaml(object):
    _service = dict()
    path = DATABASE_PATH + "config.yaml"

    @classmethod
    def instance(cls):
        """Method  instance
        :return: cls
        """
        instance = cls._service.get(cls.__name__, None)
        if not instance:
            instance = cls.__new__(cls)
            cls._service.setdefault(cls.__name__, instance)
        return instance

    def parse(self, section="write_postgres"):
        """
        根据环境变量进行解析, 不同环境下数据库的yaml解析配置
        :param section: 获取 section 对应的数据
        :return:
        """
        # profile 标识开发环境还是测试环境
        try:
            if profile == 'dev':
                _profile = "dev"
            elif profile == 'test':
                _profile = 'test'
            else:
                _profile = "prod"
            f = open(self.path, encoding='UTF-8')
            content = yaml.safe_load(f)
            _section = content.get(_profile).get(section)
            return _section
        except Exception as e:
            raise e

    def app_parse(self, section='page'):
        """
            yaml解析
            :param section: 获取 section 对应的数据
            :return:
        """
        try:
            f = open(self.path, encoding='UTF-8')
            content = yaml.safe_load(f)
            _section = content.get("app").get(section)
            return _section
        except Exception as e:
            raise e


if __name__ == '__main__':
    parse_yaml = ParseYaml().instance()
    print(parse_yaml.app_parse())
