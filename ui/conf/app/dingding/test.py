#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test.py
@time:2021/05/01
"""
import yaml

with open('main_page.yml', encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    print(datas['login'])