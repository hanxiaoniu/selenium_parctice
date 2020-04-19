#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/19 8:10 下午
#@Author: chloehan
#@File  : base_page.py
'''完成对通用代码的引入,例如驱动等'''
from selenium import webdriver


class BasePage:
    def __init__(self, driver=None):
        if driver==None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.get(self._base_url)
        else:
            self.driver = driver
