# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 17:20
# @Author  : lance
# @File    : area.py
# @Software: PyCharm
"""
record模块api文档
"""

"""
    @api {post} /yzg_openapi/record     条件查询上传记录
    @apiVersion 1.0.0
    @apiGroup Record
    @apiDescription 需要token,begin_time end_time 不填获取全部数据
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "begin_time":"2019-03-04 15:42:20",
        "end_time":"2019-03-04 15:45:30",
        "page_num":1,
        "offset":10
    }
    @apiSuccess {String} upload_context      上传报文
    @apiSuccess {String} response_result      响应结果
    @apiSuccess {Number} response_sign       响应结果标识 0:失败　1:成功  
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！",
        "data": {
            "result": [
                {
                    "create_time": "2019-03-04 15:45:30",
                    "upload_context": "sdsadsa",
                    "response_result": "asdasdas",
                    "response_sign": 0
                }
            ],
            "count": 1
        }
    }
"""
