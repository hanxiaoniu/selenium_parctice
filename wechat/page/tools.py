#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/25 4:37 下午
#@Author: chloehan
#@File  : tools.py
'''管理工具page'''
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage


class Tools(BasePage):
    def join_member(self):
        '''成员加入'''
        self.find((By.LINK_TEXT, "成员加入")).click()
        pass
