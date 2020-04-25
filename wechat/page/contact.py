#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/18 11:59 下午
# @Author: chloehan
# @File  : contact.py
"""
目录
定义一些方法/功能
"""
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button = (By.ID, 'SSSS')

    def add_member(self, data):
        '''添加成员，需传入数据data'''
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        self.find(name_locator).send_keys("chloehan")
        self.find(acctid_locator).send_keys("chloa")
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(mobile_locator).send_keys("123412345675")
        self.find(By.LINK_TEXT, '保存并继续添加').click()
        return self

    def add_member_error(self, data):
        return AddMemberPage()

    def search(self, data):
        '''查询功能，需传入data'''
        pass

    def import_users(self, data):
        '''导入成员'''
        pass

    def export_users(self):
        '''导出成员'''
        pass

    def set_department(self, data):
        '''设置所在部门'''
        pass

    def delete(self):
        '''删除'''
        pass

    def invite(self):
        '''微信邀请'''
        pass

    def add_department(self, data):
        '''添加部门'''
        pass

    def add_tag(self, data):
        '''添加标签'''
        pass

    def add_company(self, data):
        '''添加互联企业'''
        pass
