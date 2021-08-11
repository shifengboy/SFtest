#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_gotowork.py
@time:2020/11/19
@case:钉钉上班打卡
"""
from time import sleep

from lib.page import APP


class TestGoOffWork:
    def setup(self):
        self.app = APP()
        self.main = self.app.start()

        # 登录处理
        # try:
        #     self.main.login()
        # except Exception as e:
        #     return e



    def test_gooffwork(self):
        sleep(15)
        self.main.login()
        self.page = self.main.goto_main_page()
        self.page.goto_workbench().chose_company().clock_out()
        assert '打卡成功' in self.page.get_pagesource()
