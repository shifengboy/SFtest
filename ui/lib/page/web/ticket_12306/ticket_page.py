#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:ticket_page.py
@time:2021/05/13
"""
import os

from ui.lib.core.base import Base
from ui.lib.core.path import CONFPATH

main_page_file = CONFPATH + 'web' + os.path.sep + 'ticket_12306' + os.path.sep + 'ticket_page.yml'

class TicketPage(Base):
    def book_button(self):
        self.parse_yaml(main_page_file,'book_button',explain='预订按钮')