#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:pintuan_page.py
@time:2021/05/02
"""

import os
from lib import Base
from lib.core.path import CONFPATH

pintuan_page_file = CONFPATH + 'web' + os.path.sep + 'koubei' + os.path.sep + 'pintuan_page.yml'

class PinTuanPage(Base):

    def open_url(self):
        self.open('https://e.alipay.com/p/kb-groupbooking/index.htm?nouse=1#/create')
        return self

    def selection_button(self):
        self.parse_yaml(pintuan_page_file,'selection_button',explain='选择商品按钮')
        return self

    def item_table(self):
        self.parse_yaml(pintuan_page_file,'item_table',explain='选品列表')
        return self

    def confirm_button(self):
        self.parse_yaml(pintuan_page_file,'confirm_button',explain='确认按钮')
        return self

    def quit(self):
        self.quit_driver()