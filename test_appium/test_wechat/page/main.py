#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 主页面
from appium.webdriver.common.mobileby import MobileBy

from test_appium.test_wechat.page.addresslistpage import AddressListPage

# 主页面
from test_appium.test_wechat.page.basepage import BasePage


class MainPage(BasePage):
    _address_element = (MobileBy.XPATH, "//android.widget.TextView[@text='通讯录']")

    # 方法： 进入到通讯录
    def goto_addresslist(self):
        # 2、点击通讯录
        # self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        self.find_and_click(self._address_element)
        return AddressListPage(self.driver)

    def goto_message(self):
        pass

    def goto_workbench(self):
        pass
