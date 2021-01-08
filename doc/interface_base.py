# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 17:20
# @Author  : lance
# @File    : area.py
# @Software: PyCharm
"""
interface模块api文档
"""

"""
    @api {get} /yzg_openapi/interface_catalog     获取目录
    @apiVersion 1.0.0
    @apiGroup Interface
    @apiDescription 需要token
   
    @apiSuccessExample {json} 成功响应:
    [
      {
        "name": "接入指南",
        "url": "https://www.baidu.com/",
        "query":"guideInterven"
      },
      {
        "name": "产品手册",
        "url": "",
        "children": [
          {
            "name": "基本概念",
            "url": "https://www.baidu.com/",
            "query":"guideInterven"
          },
          {
            "name": "版本说明",
            "url": "https://www.baidu.com/",
            "query":"guideInterven"
          }
        ]
      },
      {
        "name": "api接口文档",
        "url": "",
        "children": [
          {
            "name": "项目",
            "url": "",
            "children": [
              {
                "name": "上传项目",
                "url": "https://www.baidu.com/",
                "query":"guideInterven"
              },
              {
                "name": "项目查询",
                "url": "https://www.baidu.com/",
                "query":"guideInterven"
              }
            ]
          },
          {
            "name": "企业",
            "url": "",
            "children": [
              {
                "name": "上传企业",
                "url": "https://www.baidu.com/",
                "query":"guideInterven"
              },
              {
                "name": "企业查询",
                "url": "https://www.baidu.com/",
                "query":"guideInterven"
              }
            ]
          }
        ]
      },
      {
        "name": "常见问题",
        "url": "https://www.baidu.com/",
        "query":"guideInterven"
      }
    ]
"""
