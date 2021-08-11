#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:handle_black.py
@time:2021/05/01
@功能：处理操作步骤及异常处理
"""
import allure

from ui.lib.core.path import WEBPICTUREPATH


def handle_black(func):
    def wrapper(*args,**kwargs):
        from ui.lib.core.base import Base
        instance: Base = args[0]
        explain = kwargs.get('explain')
        try:
            with allure.step(f'测试步骤：{explain}'):
                instance.driver.save_screenshot(WEBPICTUREPATH + 'tmp.png')
                allure.attach.file(WEBPICTUREPATH + 'tmp.png', attachment_type=allure.attachment_type.PNG)
                result = func(*args, **kwargs)
            instance.err_num = 0
            return result
        except Exception as e:
            instance.driver.save_screenshot(WEBPICTUREPATH + 'tmp.png')
            allure.attach.file(WEBPICTUREPATH + 'tmp.png', attachment_type=allure.attachment_type.PNG)
            if instance.err_num > instance.max_num:
                raise e
            instance.err_num += 1
            # 从黑名单中遍历元素，依次进行处理
            for black_ele in instance.black_list:
                ele = instance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理完黑名单后，再次查找原来的元素
                    return wrapper(*args, **kwargs)
            raise e

    return wrapper
