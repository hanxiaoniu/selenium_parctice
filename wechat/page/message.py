#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/25 7:10 下午
# @Author: chloehan
# @File  : message.py
"""消息群发"""
from time import sleep

from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage


class Message(BasePage):
    def send(self,app="", message="", group=""):
        self.find((By.LINK_TEXT,'选择需要发消息的应用')).click()
        self.find((By.CSS_SELECTOR,'div[data-name*="%s"]' % app)).click()
        self.find((By.LINK_TEXT, '确定')).click()

        self.find((By.LINK_TEXT, "选择发送范围")).click()
        #todo: 改成显式等待
        sleep(3)
        element=self._driver.find_elements(By.CSS_SELECTOR, ".ww_searchInput_text")[-1];
        element.send_keys(group)
        self.find((By.CSS_SELECTOR, '#searchResult li')).click()
        self.find((By.LINK_TEXT, '确认')).click()

        self.find((By.CSS_SELECTOR, "textarea.js_send_msg_text")).send_keys(content)
        self.find((By.LINK_TEXT, "发送")).click()
        self.find((By.LINK_TEXT, "确定")).click()

    def get_histrory(self):
        pass

