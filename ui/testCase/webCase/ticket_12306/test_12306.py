#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_12306.py
@time:2021/05/22
"""
import allure

from ui.lib.page.web.ticket_12306.main_page import MainPage


@allure.feature("拼团")
class Test12306:
    '''12306demo'''

    def setup(self):
        self.page = MainPage(remote=True,remote_url='http://shifeng.online:5001/wd/hub')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("查询余票")
    @allure.title('查询余票')
    def test_12306(self):
        '''查询余票case'''
        self.page.open_page().from_StationText().to_station().train_date().search_one().book_button()

    def teardown(self):
        self.page.quit_driver()