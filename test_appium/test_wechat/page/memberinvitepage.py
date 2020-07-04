#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 添加成员 页面
# from test_appium.test_wechat.page.contactaddpage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.basepage import BasePage


class MemberInvitePage(BasePage):
    _addmember_menual_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    # def __init__(self,driver):
    #     self.driver = driver

    def addmember_menual(self):
        from test_appium.test_wechat.page.contactaddpage import ContactAddPage
        # 4、选择手动添加成员
        # self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        self.find_and_click(self._addmember_menual_element)
        return ContactAddPage(self.driver)

    def get_result(self):
        # toasttext = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        toasttext = self.get_toast()
        return toasttext
