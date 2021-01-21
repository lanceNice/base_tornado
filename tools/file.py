#!/usr/bin/env python
# -*- coding:utf-8 -*-
import asyncio
import json
import os
import time
from aiofile import AIOFile, LineReader, Reader
from tools.filepath import get_conf_file_path


def remove_file(file_path):
    """
    :param file_path:  文件路径
    :return:
    """
    if os.path.exists(file_path):
        os.remove(file_path)


# 判断文件夹是否存在
def dir_is_exist(path):
    """
    :param path: 文件夹路径
    :return:
    """
    if os.path.exists(path):
        pass
    else:
        os.mkdir(path)


# 文件读取
async def file_read(file_path):
    """
    :param file_path: 文件路径
    :return:
    """
    async with AIOFile(file_path, 'r') as afp:
        # 按行返回
        # async for line in LineReader(afp):
        #     print(line[:-1])
        # 全部返回
        data_json = await afp.read()
        print(data_json)


# 文件写入
async def file_write(file_path, text):
    """
    :param file_path: 文件路径
    :param text: 文本内容
    :return:
    """
    async with AIOFile(file_path, 'wb') as afp:
        await afp.write(text.encode("utf-8"))
        await afp.fsync()


async def do():
    # file_path = get_conf_file_path("city.json")
    # await file_write(file_path, str(time.time()))
    # await file_read(file_path)
    pass


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    task = loop.create_task(do())
    loop.run_until_complete(task)
    loop.close()
