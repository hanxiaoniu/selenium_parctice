#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 1:44 上午
# @Author: chloehan
# @File  : test_index.py

from wechat.page.index import Index


class TestIndex:
    def setup(self):
        self.index = Index()

    def test_register(self):
        self.index.goto_registet().register("小萌鹅")

    def test_login(self):
        """如果不在类中返回self，代码比较冗余且难调用driver
        self.index.goto_login()
        login=Login(self.driver)
        """
        register_page=self.index.goto_login().goto_register().register("chloehanmin")
        assert "请选择" in "|" .join(register_page.get_error_message())


    def teardown(self):
        self.index.close()
