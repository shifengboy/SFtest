#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:main_page.py
@time:2021/05/11
"""
import os
from time import sleep

import yaml

from sftest import get_date
from ui.lib.core.base import Base
from ui.lib.core.path import CONFPATH
from ui.lib.page.web.ticket_12306.ticket_page import TicketPage

main_page_file = CONFPATH + 'web' + os.path.sep + 'ticket_12306' + os.path.sep + 'main_page.yml'


class MainPage(Base):
    def open_page(self):
        self.open_by_yaml(main_page_file, 'index')
        return self

    def from_StationText(self):
        self.parse_yaml(main_page_file, 'from_station', explain='选择出发地')
        return self

    def to_station(self):
        self.parse_yaml(main_page_file, 'to_station', explain='选择达到地')
        return self

    def train_date(self):
        time = get_date(offsetDay=1)[0:10]
        self.js(f'a=document.getElementById("train_date");a.removeAttribute("readonly");a.value="{time}"')
        return self

    def search_one(self):
        self.open_new_window(main_page_file, 'search_one', explain='查询车次信息')
        return TicketPage(self)


if __name__ == '__main__':
    s = MainPage()
    s.open_page().from_StationText().to_station().train_date().search_one().book_button()
