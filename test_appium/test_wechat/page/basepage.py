#!/usr/bin/env python
# -*- coding: utf-8 -*-
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

"""
basepage.py
 
用来存放一些最基本的操作
1、实例化driver 对象
2、find 方法
3、appium 层底操作
"""


class BasePage:
    driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 查找元素
    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_by_scroll(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{text}").instance(0));')

    def find_and_click(self, locator):
        self.find(locator).click()

    def get_toast(self):
        return self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text

    def back(self, num=1):
        for i in range(num):
            self.driver.back()
