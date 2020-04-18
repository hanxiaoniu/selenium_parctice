#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/4/19 12:43 上午
#@Author: chloehan
#@File  : test_main.py
from wechat.page.main import IndexMain


class TestMain:
    def test_add_member(self):
        main=IndexMain()
        main.add_member().add_member("xxx")
        # 导入成员后查看是否返回消息,然后断言
        assert "aaa" in main.import_user().get_message()