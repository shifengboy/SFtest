#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:pintuan_test.py
@time:2021/05/02
"""
import allure
from ui.lib.page.web.koubei.main_page import MainPage
from ui.lib.page.web.koubei.pintuan_page import PinTuanPage


@allure.feature("拼团")
class TestPintuan:
    '''拼团模块'''

    def setup(self):
        self.page = MainPage().login()

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("创建拼团")
    @allure.title('创建拼团标题')
    def test_creat_pintuan(self):
        '''创建商家拼团活动'''
        self.page = PinTuanPage(self.page).open_url().selection_button().item_table().confirm_button()

    def teardown(self):
        self.page.quit()

# if __name__ == '__main__':
# print(curPath)
