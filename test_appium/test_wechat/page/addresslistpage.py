#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 通讯录 页面
from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.memberinvitepage import MemberInvitePage


class AddressListPage(BasePage):
    _addmember_text = "添加成员"

    # def __init__(self,driver):
    #     self.driver = driver

    # 点击 添加成员
    def click_addmember(self):
        # 3、找到添加成员，点击添加成员
        # self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(true)\
        #     .instance(0)).scrollIntoView(new UiSelector().\
        #     text("添加成员").instance(0));').click()
        self.find_by_scroll(self._addmember_text).click()

        return MemberInvitePage(self.driver)
