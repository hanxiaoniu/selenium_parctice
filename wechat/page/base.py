#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/16 8:16 下午
# @Author: chloehan
# @File  : base.py
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Testhogwarts:
    def setup_method(self):
        """多浏览器处理，使用browser=firefox pytest wechat/page/base.py(包名/文件名.py)"""
        # browser = os.getenv("browser").lower()
        # if browser == "headless":
        #     self.driver = webdriver.PhantomJS()
        # elif browser == "chrome":
        #     """option可以自定义传入参数，headless为无UI模式,--disable-gpu禁用gpu加速,
        #     --remote-debugging-port=9222其它机器可以远程连接
        #     """
        #     options = Options()
        #     # options.add_argument("--headless")
        #     # options.add_argument("--window-size=1280,1696")
        #     # options.add_argument("--disable-gpu")
        #     # options.debugger_address("--remote-debugging-port=9222")
        #     options.debugger_address = 'localhost:9999'
        #     self.driver = webdriver.Chrome(options=options)
        #     # self.driver = webdriver.Chrome()
        # elif browser == "firefox":
        #     # options
        #     self.driver = webdriver.Firefox()
        # elif browser == "htmlunit":
        #     self.driver = webdriver.PhantomJS
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.debugger_address = '127.0.0.1:9999'
        self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
        """设置浏览器窗口大小"""
        # self.driver.set_window_size(1440,877)
        self.driver.implicitly_wait(5)

    def wait(self, timoout, method):
        """显式等待封装的方法，只需要传入(10,es.xxxx(element))即可调用"""
        WebDriverWait(self.driver, timoout).until(method)

    def test_add(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        self.driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        self.driver.find_element(By.ID,'username').send_keys("chloehan")
        self.driver.find_element(By.ID,'memberAdd_acctid').send_keys("abc")
        self.driver.find_element(By.ID,'memberAdd_phone').send_keys("12345678901")
        self.driver.find_element(By.CSS_SELECTOR,'.js_btn_save').click()

    def teardown_method(self):
        """每个case执行完之后调用的方法，退出浏览器操作"""
        self.driver.quit()
