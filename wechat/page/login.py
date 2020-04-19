#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/19 8:31 下午
#@Author: chloehan
#@File  : login.py
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage
from wechat.page.register import Register


class Login(BasePage):
    def scan_qrcode(self):
        pass

    def goto_register(self):
        self._driver.find_element(By.LINK_TEXT, '企业注册').click()
        return Register(self._driver)