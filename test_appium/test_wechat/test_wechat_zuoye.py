#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

# appium-python-client 提供api
from time import sleep

import pytest
import yaml
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

with open('../datas/contacts.yml') as f:
    datas = yaml.safe_load(f)
    print(datas)
    addlist = datas['add']
    dellist = datas['del']


class TestWechat:
    def setup_class(self):
        caps = {}
        caps["deviceName"] = "emulator-5554"
        caps["platformName"] = "Android"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        # 最重要代码，创建驱动
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def teardown_class(self):
        # 关闭这个session
        self.driver.quit()

    @pytest.mark.parametrize('username, gender, phonenum',
                             addlist
                             )
    def test_addcontact(self, username, gender, phonenum):
        """
        1、打开企业微信
        2、点击通讯录
        3、找到添加成员，点击添加成员
        4、选择手动添加成员
        5、输入姓名，性别，手机号，点击保存按钮
        6、验证保存成功（toast, 通讯录列表）
        :return:
        """
        # username = "霍格沃00"
        # gender = '女'
        # phonenum = '13800000010'
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
        self.driver.back()

    @pytest.mark.parametrize('username',
                             dellist
                             )
    def test_deletecontact(self, username):
        """
        2、点击通讯录
        3、点击 被删除的联系人
        4、点击右上角
        5、点击 【编辑成员】
        6、点击 【删除成员】
        7、点击 【确定】
        8、验证删除成功

        :return:
        """
        # username = "霍格沃00"
        # gender = '女'
        # phonenum = '13800000010'
        # 2、点击通讯录
        self.driver.find_element_by_xpath("//android.widget.TextView[@text='通讯录']").click()
        # 3、点击 被删除的联系人姓名
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
            .instance(0)).scrollIntoView(new UiSelector().\
            text("{username}").instance(0));').click()
        # 4、点击右上角
        self.driver.find_element_by_id("com.tencent.wework:id/gq0").click()

        # 5、点击 【编辑成员】
        self.driver.find_element_by_xpath("//*[@text='编辑成员']").click()
        # 6、点击 【删除成员】
        self.driver.find_element_by_android_uiautomator(
            f'new UiScrollable(new UiSelector().scrollable(true)\
                    .instance(0)).scrollIntoView(new UiSelector().\
                    text("删除成员").instance(0));').click()
        # 7、点击 【确定】
        self.driver.find_element_by_xpath("//*[@text='确定']").click()
        # 8、验证删除成功
        WebDriverWait(self.driver, 15).until_not(lambda x: x.find_element_by_xpath(f"//*[@text='{username}']"))
