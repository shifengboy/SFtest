#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_12306.py
@time:2021/05/22
"""
import allure

from ui.lib.page.web.ticket_12306.main_page import MainPage


@allure.feature("查询余票")
class Test12306:
    '''12306demo'''

    def setup(self):
        self.page = MainPage(remote=True, remote_url='http://shifeng.online:5001/wd/hub')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("打开首页story")
    @allure.title('查询余票title')
    def test_open_page(self):
        '''打开首页'''
        self.page = self.page.open_page()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("选择出发地story")
    def test_from_Station(self):
        '''选择出发地'''
        self.page = self.page.from_StationText()

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("选择到达地story")
    def test_to_station(self):
        '''选择到达地'''
        self.page = self.page.to_station()

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("选择出发日期story")
    def test_train_date(self):
        '''选择出发日期'''
        self.page = self.page.train_date()

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("查询车次信息story")
    def test_search_one(self):
        '''查询车次信息'''
        self.page = self.page.search_one()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("点击预订按钮story")
    def test_book_button(self):
        '''点击预订按钮'''
        self.page = self.page.book_button()

    def teardown(self):
        self.page.quit_driver()
