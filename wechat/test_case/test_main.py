#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2020/4/19 12:43 上午
# @Author: chloehan
# @File  : test_main.py
from wechat.page.main import IndexMain


class TestMain:
    def setup(self):
        self.main = IndexMain(reuse=True)

    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        # 导入成员后查看是否返回消息,然后断言
        assert "aaa" in self.main.import_user().get_message()

    def test_import_user(self):
        self.main.import_user("xxxx.file")
        assert "success" in self.main.get_message()

    def test_invite_user(self):
        self.main.invite_user()
        #todo:判断二维码弹窗是否返回正常
        assert '' in self.main.invite_user()

    def test_send_message(self):
        main.send_message()
        assert "" in main.get_message()
