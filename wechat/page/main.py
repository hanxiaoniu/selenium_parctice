#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 12:18 上午
# @Author: chloehan
# @File  : main.py
"""企业微信首页"""
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage
from wechat.page.contact import Contact


class IndexMain(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#index"
    def download(self):
        '''立即下载'''
        pass

    def import_user(self):
        '''导入成员'''
        return self

    def goto_app(self):
        '''前往查看'''
        pass

    def goto_company(self):
        '''验证主题信息'''
        pass

    def get_message(self):
        '''消息'''
        return ["aaa","bbb"]

    def add_member(self):
        '''添加成员 因只是一个跳转，所以实质返回的是Contact()的功能'''
        #done:click
        locator=(By.LINK_TEXT,'添加成员')
        self.find(locator).click()
        #当遇到问题/bug无法使用原生的find_element时，可以使用js。例如：解决chrome缩放比例不是100%
        self._driver.execute_script("arguments[0].click();",self.find(locator))
        return Contact()

    def import_tel(self):
        '''导入通讯里'''
        pass

    def join_member(self):
        '''成员加入'''
        pass

    def group_sendMessage(self):
        '''消息群发'''
        pass

    def customer_contact(self):
        '''客户联系'''
        pass

    def sign_in(self):
        '''打卡'''
        pass
