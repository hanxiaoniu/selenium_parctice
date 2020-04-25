#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 12:18 上午
# @Author: chloehan
# @File  : main.py
"""企业微信首页"""
from selenium.webdriver.common.by import By

from wechat.page.application import ApplicationMng
from wechat.page.base_page import BasePage
from wechat.page.contact import Contact
from wechat.page.customer import Customer
from wechat.page.tools import Tools


class IndexMain(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def download(self):
        '''立即下载'''
        self.find((By.LINK_TEXT,"立即下载")).click()
        pass

    def import_user(self,path):
        '''导入成员'''
        self.find((By.PARTIAL_LINK_TEXT, "导入成员")).click()
        self.find((By.LINK_TEXT, "批量导入")).click()
        self.find(By.ID, "js_upload_file_input").send_keys(path)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self

    def invite_user(self):
        '''发起邀请'''
        self.find(By.LINK_TEXT,"发起邀请").click()
        return self

    def goto_app(self):
        '''前往查看'''
        pass

    def goto_company(self):
        '''验证主题信息'''
        pass

    def get_message(self):
        '''消息'''
        return ["aaa", "bbb"]

    def add_member(self):
        '''添加成员 因只是一个跳转，所以实质返回的是Contact()的功能'''
        # done:click
        locator = (By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # 当遇到问题/bug无法使用原生的find_element时，可以使用js。例如：解决chrome缩放比例不是100%
        self._driver.execute_script("arguments[0].click();", self.find(locator))
        #复用浏览器,不需新开界面
        return Contact(reuse=True)

    def import_tel(self):
        '''导入通讯录'''
        self.find((By.LINK_TEXT,"导入通讯录")).click()
        #todo：return contact.批量导入.文件导入
        pass

    def join_member(self):
        '''成员加入'''
        self.find((By.PARTIAL_LINK_TEXT, "成员加入")).click()
        return Tools().join_member()
        pass

    def group_sendMessage(self):
        '''消息群发'''
        self.find((By.PARTIAL_LINK_TEXT, "消息群发")).click()
        return Tools().send_message()
        pass

    def customer_contact(self):
        '''客户联系'''
        self.find((By.PARTIAL_LINK_TEXT, "客户联系")).click()
        return Customer()

    def sign_in(self):
        '''打卡'''
        self.find((By.PARTIAL_LINK_TEXT, "打卡")).click()
        return ApplicationMng().sign_in()
