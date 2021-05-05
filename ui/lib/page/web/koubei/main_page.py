#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2021/05/02
"""
import os

from ui.lib.core.base import Base
from ui.lib.core.path import CONFPATH
from ui.lib.page.web.koubei.pintuan_page import PinTuanPage

main_page_file = CONFPATH + 'web' + os.path.sep + 'koubei' + os.path.sep + 'main_page.yml'

class MainPage(Base):

    def login(self):
        self.open('https://e.alipay.com/index.htm')
        self.switch_to_frame('loginIframe')
        self.parse_yaml(main_page_file, 'login')
        return self

    def business_menu(self):
        self.parse_yaml(main_page_file,'business_menu')
        return self

    def marketing_too_menu(self):
        self.parse_yaml(main_page_file,'marketing_too_menu')
        return self

    def item_table(self):
        self.parse_yaml(main_page_file,'item_table')
        return self

    def item_pintuan(self):
        self.parse_yaml(main_page_file,'item_pintuan')
        return self

    def create_activity_button(self):
        self.parse_yaml(main_page_file,'create_activity_button')
        return PinTuanPage(self.driver)

    def quit(self):
        self.quit_driver()





if __name__ == '__main__':
    m = MainPage()
    m.login()
