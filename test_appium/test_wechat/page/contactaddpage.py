#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 成员编辑页面
# from test_appium.test_wechat.page.memberinvitepage import MemberInvitePage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.basepage import BasePage


class ContactAddPage(BasePage):
    _username_element = (MobileBy.XPATH,
                         "//*[contains(@text, '姓名')]/../android.widget.EditText")

    _gender_element = (MobileBy.XPATH,
                       "//*[@text='性别']/..//*[@text='男']")
    _female_element = (MobileBy.XPATH, "//*[@text='女']")
    _male_element = (MobileBy.XPATH, "//*[@text='男']")

    _phonenum_element = (MobileBy.XPATH,
                         "//*[contains(@text, '手机')]/..//*[@text='手机号']")

    _save_element = (MobileBy.XPATH, "//*[@text='保存']")

    # def __init__(self,driver):
    #     self.driver = driver
    # 编辑 用户名
    def edit_username(self, username):
        # self.driver.find_element_by_xpath(
        #     "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(username)
        self.find(self._username_element).send_keys(username)

        return self

    # 编辑 性别
    def edit_gender(self, gender):
        # self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
        # self.find(self._gender_element).click()
        self.find_and_click(self._gender_element)
        if gender == '女':
            # self.driver.find_element_by_xpath("//*[@text='女']").click()
            # self.find(self._female_element).click()
            self.find_and_click(self._female_element)
        else:
            # self.driver.find_element_by_xpath("//*[@text='男']").click()
            # self.find(self._male_element).click()
            self.find_and_click(self._male_element)
        return self

    # 编辑 电话号码
    def edit_phonenum(self, phonenum):
        # self.driver.find_element_by_xpath("//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys(phonenum)
        self.find(self._phonenum_element).send_keys(phonenum)
        return self

    def click_save(self):
        from test_appium.test_wechat.page.memberinvitepage import MemberInvitePage
        # self.driver.find_element_by_xpath("//*[@text='保存']").click()
        self.find_and_click(self._save_element)
        sleep(2)
        return MemberInvitePage(self.driver)
