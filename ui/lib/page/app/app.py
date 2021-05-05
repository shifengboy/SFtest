#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:app.py
@time:2020/11/19

app.py 模块，存放app相关的一些操作。
比如 启动应用，重启应用，停止应用，登录App，进入到首页
"""
import yaml
from appium import webdriver

from ui.lib.core.appController import Controller
from ui.lib.core.base import Base
from ui.lib.page.app.dingding.main_page import MainPage
from ui.lib.core.path import APPPATH

# with open(APPPATH) as f:
#     datas = yaml.safe_load(f)
#     desired_caps = datas['desired_caps']
#     ip = datas['ip']


class APP(Base):
    def __init__(self):
        Base.__init__(self)
        self.controller = Controller()
        self.threads = []
    def start(self):
        if self.driver is None:
            self.controller.server()
            self.controller.server()
            self.controller.test_server()
            self.driver = self.controller.driver().get()
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def login(self):
        MainPage(self.driver).login()

    def restart(self):
        pass

    def stop(self):
        pass

    def close(self):
        pass

    def goto_main_page(self):
        return MainPage(self.driver)
