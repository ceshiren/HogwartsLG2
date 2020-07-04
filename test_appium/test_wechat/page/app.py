#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
app.py 主要用于 app的一些常用的操作： 启动app, 关闭app, 重启app, 进入主页面
"""
from appium import webdriver
from appium.webdriver.webdriver import WebDriver

from test_appium.test_wechat.page.basepage import BasePage
from test_appium.test_wechat.page.main import MainPage


class App(BasePage):
    driver: WebDriver

    # 启动app
    def start(self):
        if self.driver == None:
            caps = {}
            caps["deviceName"] = "emulator-5554"
            caps["platformName"] = "Android"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            # 最重要代码，创建驱动
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            # launch_app() 启动的是desirecap里面定义的 activity
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def close(self):
        self.driver.quit()

    # 进入到主页
    def main(self):
        return MainPage(self.driver)
