#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:baapp.py
@time:2021/05/02
"""
from appium.webdriver import WebElement
from appium.webdriver.connectiontype import ConnectionType
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from lib.core.base import Base
from lib.core.handle import handle
from lib.core.logger import logger


class Baseapp(Base):
    def __init__(self, driver):
        self.driverriver = driver

    def swipe_up(self, t=500, n=1):
        '''
        向上滑动屏幕
        :param t: 滑动速度
        :param n: 滑动次数
        :return:
        '''
        l = self.driverriver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.85  # 起始y坐标
        y2 = l['height'] * 0.25  # 终点y坐标
        for i in range(n):
            self.driverriver.swipe(x1, y1, x1, y2, t)

    def swipe_down(self, t=500, n=1):
        '''
        向下滑动屏幕
        :param t: 滑动速度
        :param n: 滑动次数
        :return:
        '''
        l = self.driverriver.get_window_size()
        x1 = l['width'] * 0.5  # x坐标
        y1 = l['height'] * 0.25  # 起始y坐标
        y2 = l['height'] * 0.75  # 终点y坐标
        for i in range(n):
            self.driverriver.swipe(x1, y1, x1, y2, t)

    def swipe_left(self, t=500, n=1):
        '''
        向左滑动屏幕
        :param t: 滑动速度
        :param n: 滑动次数
        :return:
        '''
        l = self.driverriver.get_window_size()
        x1 = l['width'] * 0.75
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.05
        for i in range(n):
            self.driverriver.swipe(x1, y1, x2, y1, t)

    def swipe_right(self, t=500, n=1):
        '''
        向右滑动屏幕
        :param t: 滑动速度
        :param n: 滑动次数
        :return:
        '''
        l = self.driverriver.get_window_size()
        x1 = l['width'] * 0.05
        y1 = l['height'] * 0.5
        x2 = l['width'] * 0.75
        for i in range(n):
            self.driverriver.swipe(x1, y1, x2, y1, t)

    @handle
    def find(self, by, locator=None, timeout=10, *args, **kargs) -> WebElement:
        '''
        判断元素是否可点击
        :param by:
        :param locator:
        :return:
        '''
        logger.debug(f'find.by:{by}')
        logger.debug(f'find.locator:{locator}')
        if locator is None:
            result = WebDriverWait(self.driverriver, timeout=timeout).until(
                expected_conditions.element_to_be_clickable(*by))
        else:
            result = WebDriverWait(self.driverriver, timeout=timeout).until(
                expected_conditions.element_to_be_clickable((by, locator)))

        return result

    def key_code(self, code):
        '''
        :param code: 按键码
        :return:
        '''
        self.driverriver.press_keycode(code)
        
    def hide_keyboard(self):
        self.driverriver.hide_keyboard()
        
    def background_app(self, second):
        self.driver.background_app(second)

    @property
    def current_context(self):
        return self.driver.current_context

    @property
    def context(self):
        return self.driver.context

    @property
    def contexts(self):
        return self.driver.contexts

    def switch_web_view(self):
        context_names = self.contexts
        if context_names > 1:
            self.driver.switch_to.context(context_names[-1])

    def switch_native_app(self):
        context_names = self.contexts
        self.driver.switch_to.context(context_names[0])

    def set_network(self, network):
        '''
        1、WIFI 2、数据流量 3、飞行模式 4、无网 5、全部打开
        '''
        if network == 1:
            self.driver.set_network_connection(ConnectionType.WIFI_ONLY)
        elif network == 2:
            self.driver.set_network_connection(ConnectionType.DATA_ONLY)
        elif network == 3:
            self.driver.set_network_connection(ConnectionType.AIRPLANE_MODE)
        elif network == 4:
            self.driver.set_network_connection(ConnectionType.NO_CONNECTION)
        elif network == 5:
            self.driver.set_network_connection(ConnectionType.ALL_NETWORK_ON)
        return self

    def launch_app(self):
        return self.driver.launch_app()

    def close_app(self):
        return self.driver.close_app()

    def reset(self):
        return self.driver.reset()

    def is_app_installed(self, package):
        return self.driver.is_app_installed(package)

    def set_value(self, element, value):
        self.driver.set_value(element, value)

    def lock(self, s):
        self.driver.lock(s)

if __name__ == '__main__':
    a = Baseapp()
