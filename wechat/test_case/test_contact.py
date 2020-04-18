#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/19 12:12 上午
#@Author: chloehan
#@File  : test_contact.py
from wechat.page.contact import Contact


class TestContact:
    def test_add_user(self):
        contact=Contact()
        contact.add_member("chloehan")
        contact