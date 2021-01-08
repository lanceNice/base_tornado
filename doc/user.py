# -*- coding: utf-8 -*-
# @Time    : 2019/9/9 17:20
# @Author  : lance
# @File    : area.py
# @Software: PyCharm
"""
user模块api文档
"""

"""
    @api {post} /yzg_openapi/login      用户登陆
    @apiVersion 1.0.0
    @apiGroup User
    @apiSuccess {String} token      用户token
    @apiSuccess {Number} type       角色类型 （1.管理员 2.普通用户）  
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "password":"111111"   
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！",
        "data": {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODQ1OTkzMDksImlhdCI6MTU4MzMwMzMwOSwiZGF0YSI6eyJ0b2tlbl9uYW1lIjoiYWNjZXNzX3Rva2VuIiwiaWQiOjEwfX0.eJnx-SRLeU1Q6l2YhZ817ytTcTxGzvubApC2GZZX4bY",
            "type": 2,
            "phone": "15738854260"
        }
    }
    
"""

"""
    @api {post} /yzg_openapi/user      用户注册
    @apiVersion 1.0.0
    @apiGroup User
    @apiDescription 需要token
    @apiParam {Number}  type        角色类型 （1.管理员 2.普通用户）
    @apiParam {String}  company_name        技术支持单位名称
    @apiParam {String}  company_socialcreditcode        技术支持单位统一社会信用代码
    @apiParam {String}  note        备注
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "type":2,
        "company_name":"杭州悦天云数据科技有限公司",
        "company_socialcreditcode":"91330106MA2CFJLN7J",
        "name":"王猛",
        "note":"后端开发",
        "yzg_address":"https://demo.yooticloud.cn",
        "yzg_city_name":"线上测试",
        "yzg_city_db":"demo"
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！"
    }
"""

"""
    @api {post} /yzg_openapi/logout      用户登出
    @apiVersion 1.0.0
    @apiGroup User
    @apiDescription 需要token
    @apiParam {String}  phone        用户手机号
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260"
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！"
    }
"""
"""
    @api {post} /yzg_openapi/sms      发送验证码
    @apiVersion 1.0.0
    @apiGroup User
    @apiParam {String}  phone        用户手机号
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260"
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！"
    }
"""

"""
    @api {post} /yzg_openapi/forget_password     忘记密码
    @apiVersion 1.0.0
    @apiGroup User
    @apiParam {String}  phone        用户手机号
    @apiParam {String}  new_password        新密码
    @apiParam {String}  v_code        验证码
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "new_password":"123456",
        "v_code":"637240"
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！"
    }
"""

"""
    @api {post} /yzg_openapi/set_password     修改密码
    @apiVersion 1.0.0
    @apiGroup User
    @apiDescription 需要token
    @apiParam {String}  phone        用户手机号
    @apiParam {String}  new_password        新密码
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "new_password":"111111"
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！"
    }
"""

"""
    @api {post} /yzg_openapi/user_list     根据手机号查询用户信息
    @apiVersion 1.0.0
    @apiGroup User
    @apiDescription 需要token
    @apiParamExample {json} 请求示例:
    {
        "phone":"15738854260",
        "page_num":1,
        "offset":10
    }
    @apiSuccessExample {json} 成功响应:
    {
        "code": 1,
        "msg": "成功！",
        "data": {
            "result": [
                {
                    "company_name": "杭州悦天云数据科技有限公司",
                    "company_socialcreditcode": "91330106MA2CFJLN7J",
                    "name": "王猛",
                    "note": "后端开发",
                    "app_id": "1583226214965160",
                    "app_key": "998472267606F181D27144CA6B99EEB1",
                    "yzg_address": "https://demo.yooticloud.cn",
                    "yzg_city_name": "线上测试"
                }
            ],
            "count": 1
        }
    }
"""
