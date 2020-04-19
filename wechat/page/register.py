#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 1:52 上午
# @Author: chloehan
# @File  : register.py
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage


class Register(BasePage):

    def register(self,data):
        self.driver.find_element(By.ID, 'corp_name').send_keys("企业名称")
        self.driver.find_element(By.ID, 'manager_name').send_keys('管理员姓名')
        self.driver.find_element(By.ID, 'register_tel').send_keys("管理员手机号")
        self.driver.find_element(By.ID,'iagree').send_keys('')
        self.driver.find_element(By.ID,'submit_btn').click()
        return self
