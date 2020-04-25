#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/25 4:37 下午
#@Author: chloehan
#@File  : tools.py
'''管理工具page'''
from selenium.webdriver.common.by import By


class Tools:
    def join_member(self):
        '''成员加入'''
        self.find((By.LINK_TEXT, "成员加入")).click()
        pass

    def send_message(self):
        '''消息群发'''
        self.find((By.LINK_TEXT, "消息群发")).click()
        pass