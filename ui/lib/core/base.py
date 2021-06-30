#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:base.py
@time:2021/05/01
"""
import os
import time

import yaml
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from sftest import *
from ui.lib.core.handle_black import handle_black
from ui.lib.core.logger import logger


class Base():
    black_list = [(By.XPATH, '//*[@class="btn2"]')]
    max_num = 3
    err_num = 0

    def __init__(self, driver: WebElement = None, browser='chrome', env=None, remote=False, remote_url=None):
        '''
        运行类初始化方法，默认使用来Chrome浏览器。当然，你也可以传递参数为其他浏览器。
        '''
        self.env = env
        self.remote = remote
        self.remote_url = remote_url
        self.browser = browser
        browser = self.get_browser
        if driver == None:
            remote_url = self.get_remote
            if remote_url is not None:
                driver = webdriver.Remote(remote_url)
            elif browser == "firefox" or browser == "ff":
                driver = webdriver.Firefox()
            elif browser == "chrome":
                option = webdriver.ChromeOptions()
                option.add_argument("--start-maximized")
                driver = webdriver.Chrome(chrome_options=option)
            elif browser == "internet explorer" or browser == "ie":
                driver = webdriver.Ie()
            elif browser == "opera":
                driver = webdriver.Opera()
            elif browser == "phantomjs":
                driver = webdriver.PhantomJS()
            elif browser == 'edge':
                driver = webdriver.Edge()
            try:
                if remote:
                    logger.debug(f'本次使用远程hub节点{remote_url}运行行自动化测试')
                else:
                    logger.debug(f'本次使用{browser}浏览器进行自动化测试')
                self.driver = driver
                self.driver.maximize_window()
            except Exception:
                logger.debug(
                    "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)
                raise NameError(
                    "Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)
        else:
            self.driver = driver

    @property
    def get_remote(self):
        #     获取远程节点
        remote_url = None
        try:
            remote = self.remote
            if remote:
                remote_url = self.remote_url
                if remote_url is None:
                    remote_url = os.environ.get("remote")
                logger.debug(f'获取到远程节点{remote_url}')
            else:
                remote = os.environ.get("remote")
                if remote:
                    remote_url = os.environ["remote_url"]
                    logger.debug(f'获取到远程节点{remote_url}')
                else:
                    logger.debug('不启用远程节点配置')
        except Exception:
            logger.debug('获取远程节点出现未知异常！')
            raise Exception
        return remote_url

    @property
    def get_browser(self):
        #     获取浏览器
        browser = os.environ.get('browser')
        if browser is None:
            browser = self.browser
        return browser

    def open(self, url):
        '''
        打开连接
        :param url:
        :return:url_name
        '''
        logger.debug(f'打开链接{url}')
        self.driver.get(url)

    @property
    def get_env(self):
        # 获取测试环境
        try:
            env = os.environ["env"]
            logger.debug(f'本次UI自动化运行环境为{env}环境')
        except KeyError:
            env = self.env
            if env is None:
                env = 'prod'
                logger.debug(f'没有配置测试环境, 默认在生产环境{env}进行自动化测试')
            else:
                logger.debug(f'本次UI自动化运行环境为{env}环境')
        return env

    def open_by_yaml(self, path, url_name, func_name='url'):
        """
        打开连接
        Args:
            path:yml文件路径
            url_name:路径名
            func_name:路径所在的方法名

        Returns:

        """
        env = self.get_env
        with open(path, encoding='UTF-8') as f:
            datas = yaml.safe_load(f)
            data_env = datas['env']
            if env in data_env:
                url_base = data_env[env]
                logger.debug(f'在配置中找到环境{env}，开始运行')
            else:
                logger.error(f'在配置中未找到环境{env}，请配置该环境活动确认环境是否正确')
                raise Exception('环境有误！')
            steps = datas[func_name]
            for step in steps:
                if url_name in step:
                    url_relative = step[url_name]
                    url = url_base + url_relative
                    logger.debug(f'打开链接:{url}')
                    return self.driver.get(url)
            else:
                logger.error(f'链接打开失败，请检查链接名{url_name}是否正确！')
                raise Exception(f'链接打开失败，请检查链接名{url_name}是否正确！')

    def quit_driver(self):
        self.driver.quit()

    def find(self, by, locator=None, timeout=20, *args, **kargs) -> WebElement:
        '''
        判断元素是否可点击
        :param by:
        :param locator:
        :return:
        '''
        logger.debug(f'查找元素:（{by}，{locator}）')
        # time.sleep(0.5)  # 手动延时，避免点击过快
        if locator is None:
            try:
                result = WebDriverWait(self.driver, timeout).until(expected_conditions.element_to_be_clickable(*by))
            except Exception:
                result = WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(*by))
        else:
            try:
                result = WebDriverWait(self.driver, timeout).until(
                    expected_conditions.element_to_be_clickable((by, locator)))
            except Exception:
                result = WebDriverWait(self.driver, timeout).until(
                    expected_conditions.presence_of_element_located((by, locator)))
        logger.debug(f'查找元素结果：{result}')
        return result

    def finds(self, by, locator=None, timeout=20, *args, **kargs) -> list[WebElement]:
        '''
        判断元素是否可点击
        :param by:
        :param locator:
        :return:
        '''
        logger.debug(f'查找元素集:（{by}，{locator}）')

        if locator is None:
            elements: list[WebElement] = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(*by))
        else:
            elements: list[WebElement] = WebDriverWait(self.driver, 10).until(lambda x: x.find_elements(by, locator))

        logger.debug(f'查找元素结果集：{elements}')
        return elements

    def parse_yaml(self, path, func_name, *args, **kargs):
        '''
        解析yml文件数据
        :param path:
        :param func_name:
        :param args:
        :param kargs:
        :return:
        '''
        logger.debug(f'解析yml文件的路径:{path}，方法名：{func_name}')
        with open(path, encoding='UTF-8') as f:
            datas = yaml.safe_load(f)
            self.parse(datas[func_name], *args, **kargs)

    @handle_black
    def parse(self, steps, *args, **kargs):
        '''
        操作元素
        :param steps:
        :param args:
        :param kargs:
        :return:
        '''
        for step in steps:
            by = step['by']
            locator = step['locator']
            action = step['action']
            logger.debug(f'对元素({by}，{locator}）,进行{action}操作')
            try:
                if 'clear' in action:  # 清除输入框
                    self.find(by, locator, *args, **kargs).clear()
                if 'click' in action:  # 点击元素
                    self.find(by, locator, *args, **kargs).click()
                if 'send_keys' in action:  # 输入内容
                    self.find(by, locator, *args, **kargs).send_keys(self.function_analysis(step['context']))
                if 'right_click' in action:  # 右击
                    el = self.find(by, locator, *args, **kargs)
                    ActionChains(self.driver).context_click(el).perform()
                if 'double_click' in action:  # 双击
                    el = self.find(by, locator, *args, **kargs)
                    ActionChains(self.driver).double_click(el).perform()
                if 'drag_and_drop' in action:  # 拖拽
                    el = self.find(by, locator, *args, **kargs)
                    target = self.find(step['by'], step['locator_target'], *args, **kargs)
                    ActionChains(self.driver).drag_and_drop(el, target).perform()
                if 'clicks' in action:  # 点击所有元素
                    eles = self.finds(by, locator, *args, **kargs)
                    for ele in eles:
                        # 部分元素无法点击时，不报错
                        try:
                            ele.click()
                        except Exception:
                            pass
            except Exception as e:
                logger.debug(f'对元素({by}，{locator}）,进行{action}操作时出现错误：{e}')
                raise e

    def function_analysis(self, funtion):
        '''函数解析

        Usage:
        function_analysis('shifeng$get_date()')
        '''
        s = funtion
        if s.find('$') != -1:
            if s.find('{') != -1 and s.find('}') != -1:
                fun = s.split('{')[1].split('}')[0]
                s_new = s.split('$')[0] + eval(fun) + s.split('}')[1]
            else:
                fun = s.split('$')[1]
                s_new = s.split('$')[0] + eval(fun)
        else:
            s_new = s
        return s_new

    def js(self, script):
        '''
        执行js脚本.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        logger.debug(f'执行脚本:{script}')
        self.driver.execute_script(script)

    def move_to_right_continued(self, element, number=10):
        '''
        点击某元素，并连续点击右键，解决表格右滑问题
        Args:
            element: 点击的元素
            number: 需要点右键的次数。默认10

        Returns:

        '''
        for i in range(number):
            ActionChains(self.driver).click_and_hold(element).send_keys(Keys.RIGHT).perform()

    def switch_to_frame(self, locator):
        '''
        网页frame处理
        :param locator:
        :return:
        '''
        return self.driver.switch_to.frame(locator)

    def get_pagesource(self):
        return self.driver.page_source

    def save_screenshot(self, filename):
        return self.driver.save_screenshot(filename)

    def get_attribute(self, by, locator=None, **kargs):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("by","locator","attribute")
        '''
        el = self.find(by, locator)
        return el.get_attribute(kargs.get('attribute'))

    def get_text(self, by, locator=None):
        '''
        Get element text information.

        Usage:
        driver.get_text("by","locator")
        '''
        el = self.find(by, locator)
        return el.text

    def get_display(self, by, locator=None):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("by","locator")
        '''
        el = self.find(by, locator)
        return el.is_displayed()

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title

    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url

    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()

    def refresh(self):
        self.driver.refresh()

    def switch_to_frame_out(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        '''
        self.driver.switch_to.default_content()

    def open_new_window(self, path, func_name, *args, **kargs):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        self.parse_yaml(path, func_name, *args, **kargs)
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def assert_result(self, element, timeout=20):
        '''
        断言
        :param element:
        :param timeout:
        :return:
        '''
        result = WebDriverWait(self.driver, timeout).until(lambda x: element in x.page_source)  # 解决手机卡顿造成的误判
        logger.info(f'断言结果：{result}')
        return result

    def time_sleep(self,time=3):
        '''
        强制时间等待
        :param time: 要等待的时间
        :return:
        '''
        sleep(time)
        return self



if __name__ == '__main__':
    with open('/ui/conf/web/ticket_12306/inside_admin_page.yml', encoding='UTF-8') as f:
        datas = yaml.safe_load(f)
        print(datas['env'])
        if 'dev2' in datas['env']:
            print("ok")
