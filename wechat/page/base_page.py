#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 8:10 下午
# @Author: chloehan
# @File  : base_page.py
'''完成对通用代码的引入,例如驱动等'''
from time import sleep

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # index界面会使用，因为无传参
            self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
            self._driver.get(self._base_url)
        else:
            # Login与Register等需要用，因为有传参
            self._driver = driver

    def close(self):
        sleep(10)
        self._driver.quite()
