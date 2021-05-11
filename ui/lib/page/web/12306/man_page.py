#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:man_page.py
@time:2021/05/11
"""
import os
from time import sleep

import yaml

from ui.lib.core.base import Base
from ui.lib.core.path import CONFPATH

main_page_file = CONFPATH + 'web' + os.path.sep + '12306' + os.path.sep + 'main_page.yml'

class MainPage(Base):
    def fromStationText(self):
        self.open_by_yaml(main_page_file,'index')
        # self.open('https://www.12306.cn/index/')
        # self.parse_yaml(main_page_file,'from_station')



if __name__ == '__main__':
    MainPage().fromStationText()
    sleep(5)
