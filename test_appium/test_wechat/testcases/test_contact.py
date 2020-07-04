#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import yaml

from test_appium.test_wechat.page.app import App

with open('../datas/contacts.yml') as f:
    datas = yaml.safe_load(f)
    print(datas)
    addlist = datas['add']
    dellist = datas['del']


class TestWeWork:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().main()

    @pytest.mark.parametrize('username, gender, phonenum',
                             addlist)
    def test_addcontact(self, username, gender, phonenum):
        # username = "霍格沃02"
        # gender = '女'
        # phonenum = '13800000012'
        # 添加联人的业务逻辑
        toast = self.main.goto_addresslist() \
            .click_addmember().addmember_menual() \
            .edit_username(username).edit_gender(gender).edit_phonenum(phonenum) \
            .click_save().get_result()

        assert '添加成功' == toast
        self.main.back()

    @pytest.mark.parametrize('username',
                             dellist)
    def test_delcontact(self, username):
        self.main.goto_addresslist()

    def teardown_class(self):
        self.app.close()
