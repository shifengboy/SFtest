#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_12306.py
@time:2021/05/22
"""
import allure
import pytest

from ui.lib.page.web.ticket_12306.main_page import MainPage




@allure.feature("查询余票")
class Test12306:
    '''12306demo'''
    #
    def setup_class(self):
        # self.page = MainPage(remote=True, remote_url='http://shifeng.online:5001/wd/hub')
        self.page = MainPage()


    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("查询余票story")
    @allure.title('查询余票title')
    @pytest.mark.flaky(reruns=3, reruns_delay=2)
    def test_query_tickets(self):
        '''查询余票'''
        self.page = self.page.open_page().from_StationText().to_station().train_date().search_one().book_button()


    def teardown_class(self):
        self.page.quit_driver()
