#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 1:52 上午
# @Author: chloehan
# @File  : register.py
from selenium.webdriver.common.by import By

from wechat.page.base_page import BasePage


class Register(BasePage):

    def register(self, data):
        self._driver.find_element(By.ID, 'corp_name').send_keys("企业名称")
        self._driver.find_element(By.ID, 'manager_name').send_keys('管理员姓名')
        self._driver.find_element(By.ID, 'register_tel').send_keys("管理员手机号")
        self._driver.find_element(By.ID, 'iagree').send_keys('')
        self._driver.find_element(By.ID, 'submit_btn').click()
        # 返回类实力对象是为了链式调用？只是刚好可以做链式调用，主要是为了能继续调用此类的其它方法
        return self

    def get_error_message(self):
        '''注册失败时返回信息,拼接成一个list，供断言调用'''
        error_result = []
        for element in self._driver.find_element(By.CSS_SELECTOR, '.js_error_msg'):
            error_result.append(element.text)
            return error_result
