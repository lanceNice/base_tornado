#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import yaml

base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DATABASE_PATH = base_dir + '/conf/'


class ParseYaml(object):
    _service = dict()
    path = DATABASE_PATH + "config.yaml"
    profile = "test"

    # 获取一个单例对象
    @classmethod
    def instance(self, profile):
        """Method  instance
        :return: cls
        """
        instance = self._service.get(self.__name__, None)
        if not instance:
            instance = self.__new__(self)
            self._service.setdefault(self.__name__, instance)
        self.profile = profile
        return instance

    def parse(self, section="write_postgres"):
        """
        根据环境变量进行解析, 不同环境下数据库的yaml解析配置
        :param section: 获取 section 对应的数据
        :return:
        """
        # profile 标识开发环境还是测试环境
        try:
            if self.profile == 'dev':
                _profile = "dev"
            elif self.profile == 'test':
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
    parse_yaml = ParseYaml().instance("prod")
    print(parse_yaml.parse())
