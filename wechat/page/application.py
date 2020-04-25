#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/25 4:48 下午
# @Author: chloehan
# @File  : application.py
"""应用管理page"""
from selenium.webdriver.common.by import By


class ApplicationMng:

    def applets(self):
        '''小程序'''
        pass

    def sign_in(self):
        self.find((By.PARTIAL_LINK_TEXT, "打卡")).click()
