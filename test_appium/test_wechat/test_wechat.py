#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# appium-python-client 提供api
from time import sleep

from appium import webdriver


class TestWechat:
    def setup(self):
        caps = {}
        caps["deviceName"] = "emulator-5554"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 最重要代码，创建驱动
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        # 关闭这个session
        self.driver.quit()

    def test_demo(self):
        # 操作手机设备，完成 自动化流程
        # el1 = self.driver.find_element_by_xpath(
        #     "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[3]/android.widget.TextView")
        # el1.click()
        # 如果页面上有多个相同id， find_element_by_id 会找到第一个id进行操作
        # self.driver.find_element_by_id("com.tencent.wework:id/dnj").click()
        # eles = self.driver.find_elements_by_id("com.tencent.wework:id/dnj")
        # print(eles)
        # print(len(eles))
        # eles[5].click()
        # 通过 uiautomator定位 "通讯录"
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("通讯录")')
        sleep(3)

    def test_addcontact(self):
        """
        1、打开企业微信
        2、点击通讯录
        3、找到添加成员，点击添加成员
        4、选择手动添加成员
        5、输入姓名，性别，手机号，点击保存按钮
        6、验证保存成功（toast, 通讯录列表）
        :return:
        """
        username = "霍格沃00"
        gender = '女'
        phonenum = '13800000010'
        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        # 3、找到添加成员，点击添加成员
        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("添加成员").instance(0));').click()
        # 4、选择手动添加成员
        self.driver.find_element_by_xpath("//*[@text='手动输入添加']").click()
        # 5、输入姓名，性别，手机号，点击保存按钮
        self.driver.find_element_by_xpath(
            "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys(username)
        # 设置性别
        self.driver.find_element_by_xpath("//*[@text='性别']/..//*[@text='男']").click()
        if gender == '女':
            self.driver.find_element_by_xpath("//*[@text='女']").click()
        else:
            self.driver.find_element_by_xpath("//*[@text='男']").click()

        self.driver.find_element_by_xpath("//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys(phonenum)
        self.driver.find_element_by_xpath("//*[@text='保存']").click()

        sleep(2)
        print(self.driver.page_source)
        toasttext = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        assert toasttext == '添加成功'
