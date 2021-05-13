#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:sftest.py
@time:2021/05/12
@功能：存放一些公共方法
"""

import datetime


def get_date(offsetDay=0):
    today = datetime.datetime.now()
    # 计算偏移量
    offset = datetime.timedelta(days=+offsetDay)
    # 获取想要的日期的时间
    re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
    return re_date



if __name__ == '__main__':
    print(get_date(offsetDay=1)[0:10])
    print(type(str(get_date(offsetDay=1)[0:10])))
