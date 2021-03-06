#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 1:41 上午
# @Author: chloehan
# @File  : index.py
'''企业微信主页，未登录状态。有登录、注册、下载三个功能'''
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage
from wechat.page.login import Login
from wechat.page.register import Register


class Index(BasePage):
    _base_url="https://work.weixin.qq.com/"

    def goto_registet(self):
        '''立即注册'''
        self.find((By.LINK_TEXT, '立即注册')).click()
        return Register(self._driver)

    def goto_login(self):
        '''登录'''
        self.find((By.LINK_TEXT, '企业登录')).click()
        return Login(self._driver)
        pass

    def downloadAPP(self):
        '''下载'''
        pass
