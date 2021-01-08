### 项目描述
   云住工开放平台管理平台项目

### 响应通用标识说明

**正确响应**

    code：1

**错误响应**

|错误码  |说明  |操作建议  |
| --- | --- | --- |
|-1  |失败  |  |
|1  |成功  |  |
|400  |请求错误  |  |
|401  |当前请求需要用户验证！  |  |
|403  |禁止访问  |  |
|404  |该请求不存在  |  |
|500  |服务器错误  |  |
|502  |网关错误  |  |
|503  |服务不可达  |  |
|504  |网关超时  |  |
|10100  |参数错误  |  |
|10101  |参数验证失败  |  |
|10102  |传入指定接口的参数！  |  |
|10103  |响应数据错误  |  |
|10104  |数据校验失败  |  |
|10105  |请求参数不能为空！  |  |
|10106  |未查询到结果！！  |  |
|10110  |登录 过期！  |  |
|10111  |TOKEN 错误！  |  |
|10112  |TOKEN 必须添加！  |  |
|10113  |TOKEN 格式错误！  |  |
|10114  |TOKEN 无效！  |  |
|10301  |响应数据异常！  |  |
|10302  |数据校验失败  |  |
|10305  |请求参数不能为空！  |  |

{
    "code": -1,
    "message": "失败"
}

### 接口说明
token 需要加到header里面key为 Authorization token前面需要添加（YTC+空格）来区分

    示例：YTC eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODQ1OTc1MjgsImlhdCI6MTU4MzMwMTUyOCwiZGF0YSI6eyJ0b2tlbl9uYW1lIjoiYWNjZXNzX3Rva2VuIiwiaWQiOjEwfX0.Y9WUEREXjYXX3AaNmRzgnmk7XMJuE1I37Epkx1TMl2s




### 分页参数说明
|参数  |说明  |默认参数  |
| --- | --- | --- |
|offset  |每页显示的条数  |  10|
|page_num  |当前页数  |  1|
    

### 测试接口地址
http://192.168.0.134:8010 + 接口名

### 用户类型 
1: 管理员
2: 普通用户

### 辅助接口
1.获取落地城市接口 https://hzbj.yooticloud.cn/yzg/db/list








    





