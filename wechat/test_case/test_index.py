#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 1:44 上午
# @Author: chloehan
# @File  : test_index.py

from wechat.page.index import Index


class TestIndex:
    def setup(self):
        self.index=Index()

    def test_register(self):
        self.index.goto_registet().register("霍格沃茨测试学院")
