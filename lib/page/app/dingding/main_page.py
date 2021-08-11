#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2020/11/19
@tip：由于我们只需部分功能，故本次把所有所需功能都放入本页面内，不做多个页面的封装
"""
import os

from lib import Base
from lib.core.path import CONFPATH

main_page_file = CONFPATH + 'dingding' + os.path.sep + 'main_page.yml'

class MainPage(Base):

    def login(self):
        self.parse_yaml(main_page_file, 'login')

    def goto_workbench(self):
        self.parse_yaml(main_page_file, 'goto_workbench')
        return self

    def chose_company(self):
        self.parse_yaml(main_page_file, 'chose_company')
        return self

    def goto_attendance(self):
        self.parse_yaml(main_page_file, 'goto_attendance')
        return self

    def clock_in(self):
        self.parse_yaml(main_page_file, 'clock_in')

    def clock_out(self):
        self.parse_yaml(main_page_file, 'clock_out')

    def update_clock_out(self):
        self.parse_yaml(main_page_file, 'update_clock_out')


if __name__ == '__main__':
    print(main_page_file)