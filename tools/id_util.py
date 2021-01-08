#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @File : id_util.py 
# @Author: wyg 
# @Date : 2019-07-18 
# @Desc :

import datetime
import struct
from bson import ObjectId


def get_uuid_1():
    """
    
    :return: 201907180946536922236835
    """
    return datetime.datetime.now().strftime("%Y%m%d%H%M%S") + \
           '%.10d' % int(str(struct.unpack('>Q', ObjectId().binary[-8:])[0])[-10:])