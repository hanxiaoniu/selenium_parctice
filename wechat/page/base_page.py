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
    def __init__(self, driver: WebDriver = None, reuse=False):

        if driver == None:
            if reuse:
                options = webdriver.ChromeOptions()
                # sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9999
                options.add_argument('--ignore-certificate-errors')
                options.debugger_address = '127.0.0.1:9999'
                self._driver = webdriver.Chrome(chrome_options=options)
            else:
                # index界面会使用，因为无传参
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)

        else:
            # Login与Register等需要用，因为有传参
            self._driver = driver

        # 每个界面的url传参不一样，需要单独判断是否传了url的值
        if self._base_url != "":
            self._driver.get(self._base_url)

    def find(self, locator):
        """封装find_element,locator为定位符"""
        # isinstance()
        self._driver.find_element(*locator)

    # def find0(self,by,locator):
    #     """不需要拆箱的封装"""
    #     self._driver.find_element(locator)

    def close(self):
        sleep(10)
        self._driver.quite()
