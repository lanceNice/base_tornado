#!/usr/bin/env python
# -*- coding:utf-8 -*-

import redis
from tools.logger import logger
from conf.constant import redis as _redis
HOST = _redis.get("host", "127.0.0.1")
PORT = _redis.get("port", 6379)
REDIS_PASSWORD = _redis.get("password")
MAX_CONNECTIONS = _redis.get("max_connections", 300)


class RedisHelper(object):
    def __init__(self, db=1, host=HOST, port=PORT, redis_password=REDIS_PASSWORD, max_connections=MAX_CONNECTIONS):
        try:
            pool = redis.ConnectionPool(host=host, port=port, db=db, password=redis_password,
                                        max_connections=max_connections, decode_responses=True)
            self.__redis = redis.StrictRedis(connection_pool=pool)
        except Exception as e:
            logger.error("redis 连接失败：%s" % e)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return False

    def set(self, key, value, ex=None):
        try:
            return self.__redis.set(key, value, ex)
        except Exception as e:
            logger.info("redis set:%s fail!" % e)
            return False

    def setnx(self, key, value):
        # Set when not exist.
        return self.__redis.setnx(key, value)

    def setex(self, key, time, value):
        # setting expired
        try:
            return self.__redis.setex(key, time, value)
        except Exception as e:
            logger.error("redis setex:%s failed!" % e)
            return ""

    def delete(self, key):
        if self.__redis.exists(key):
            return self.__redis.delete(key)
        else:
            logger.error("redis delete key:%s not exist!" % key)
            return ""

    def delete_all(self):
        keys = self.__redis.keys()
        return self.__redis.delete(*keys)

    def mset(self, *args, **kwargs):
        return self.__redis.mset(*args, **kwargs)

    def mget(self, key, *args):
        # 设定多个键值对
        return self.__redis.mget(key, *args)

    def expire(self, key, time):
        if self.exist(key):
            return self.__redis.expire(key, time)
        else:
            logger.error("redis key:%s not exist!" % key)
            return ""

    def exist(self, key):
        return self.__redis.exists(key)

    def hset(self, name, key, value):
        self.__redis.hset(name, key, value)

    def hget(self, name, key):
        if self.__redis.hexists(name, key):
            return self.__redis.hget(name, key)
        else:
            return ""

    def hmset(self, name, **mapping):
        return self.__redis.hmset(name, **mapping)

    def hmget(self, name, key, *args):
        return self.__redis.hmget(name, key, *args)

    def hexist(self, name, key):
        return self.__redis.hexists(name, key)

    def hdel(self, name, *keys):
        return self.__redis.hdel(name, *keys)

    def hgetall(self, name):
        return self.__redis.hgetall(name)

    def hlen(self, name):
        return self.__redis.hlen(name)

    def hkeys(self, name):
        return self.__redis.hkeys(name)

    def hvals(self, name):
        return self.__redis.hvals(name)

    def pipeline(self, kw):
        pipe = self.__redis.pipeline(transaction=True)
        for key, value in kw.iteritems():
            pipe.set(key, value)
        pipe.execute()

    @property
    def clean_redis(self):
        self.__redis.flushdb()  # 清空 redis
        logger.info('clean redis success!')
        return 0

    def public(self, msg):
        # 发消息订阅方
        # publish发消息加入频道chan_pub
        self.__redis.publish(self.chan_pub, msg)
        return True

    def subscribe(self):
        # 开始订阅pubsub()
        # 打开收音机
        pub = self.__redis.pubsub()

        # 调频道 subscribe
        pub.subscribe(self.chan_sub)

        # 准备接收parse_response()
        # 在次调用parse_response() 开始接收
        pub.parse_response()

        # 返回订阅变量
        return pub

    def keys(self):
        return self.__redis.keys()

    def set_lpush(self, key, *value):
        self.__redis.lpush(key, *value)

    def remove_lpop(self, key):
        self.__redis.lpop(key)

    def set_rpush(self, key, *value):
        return self.__redis.rpush(key, *value)

    def remove_rpop(self, key):
        return self.__redis.rpop(key)

    def len_list(self, key):
        return self.__redis.llen(key)

    def get_list(self, key, start, end):
        return self.__redis.lrange(key, start=start, end=end)


if __name__ == '__main__':
    _redis = RedisHelper(db=1)
    _redis.set("asd","lances")

